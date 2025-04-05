from datetime import datetime
from logging import exception
from socket import *
import struct

BUFSIZE = 4096

class FinsError(Exception):
    pass

class FinsResponseError(FinsError):
    def __init__(self, EndCode):
        self.endcode = EndCode.hex()
        if self.endcode == "0101":
            self.message = self.endcode + ": Local node not in network"
        elif self.endcode == "0102":
            self.message = self.endcode + ": Token timeout"
        elif self.endcode == "0103":
            self.message = self.endcode + ": Retries failed"
        elif self.endcode == "0104":
            self.message = self.endcode + ": Too many send frames"
        elif self.endcode == "0105":
            self.message = self.endcode + ": Node address range error"
        elif self.endcode == "0106":
            self.message = self.endcode + ": Node address duplication"
        elif self.endcode == "0201":
            self.message = self.endcode + ": Destination node not in network"
        elif self.endcode == "0202":
            self.message = self.endcode + ": Unit missing"
        elif self.endcode == "0203":
            self.message = self.endcode + ": Third node missing"
        elif self.endcode == "0204":
            self.message = self.endcode + ": Destination node busy"
        elif self.endcode == "0205":
            self.message = self.endcode + ": Response timeout"
        elif self.endcode == "0301":
            self.message = self.endcode + ": Communications controller error"
        elif self.endcode == "0302":
            self.message = self.endcode + ": CPU Unit error"
        elif self.endcode == "0303":
            self.message = self.endcode + ": Controller error"
        elif self.endcode == "0304":
            self.message = self.endcode + ": Unit number error"
        elif self.endcode == "0401":
            self.message = self.endcode + ": Undefined command"
        elif self.endcode == "0402":
            self.message = self.endcode + ": Not supported by model/version"
        elif self.endcode == "0501":
            self.message = self.endcode + ": Destination address setting error"
        elif self.endcode == "0502":
            self.message = self.endcode + ": No routing tables"
        elif self.endcode == "0503":
            self.message = self.endcode + ": Routing table error"
        elif self.endcode == "0504":
            self.message = self.endcode + ": oo many relays"
        elif self.endcode == "1001":
            self.message = self.endcode + ": Command too long"
        elif self.endcode == "1002":
            self.message = self.endcode + ": Command too short"
        elif self.endcode == "1003":
            self.message = self.endcode + ": Elements/data don’t match"
        elif self.endcode == "1004":
            self.message = self.endcode + ": Command format error"
        elif self.endcode == "1005":
            self.message = self.endcode + ": Header error"
        elif self.endcode == "1101":
            self.message = self.endcode + ": Area classification missing"
        elif self.endcode == "1102":
            self.message = self.endcode + ": Access size error"
        elif self.endcode == "1103":
            self.message = self.endcode + ": Address range error"
        elif self.endcode == "1104":
            self.message = self.endcode + ": Address range exceeded"
        elif self.endcode == "1106":
            self.message = self.endcode + ": Program missing"
        elif self.endcode == "1109":
            self.message = self.endcode + ": Relational error"
        elif self.endcode == "110A":
            self.message = self.endcode + ": Duplicate data access"
        elif self.endcode == "110B":
            self.message = self.endcode + ": Response too long"
        elif self.endcode == "110C":
            self.message = self.endcode + ": Parameter error"
        elif self.endcode == "2002":
            self.message = self.endcode + ": Protected"
        elif self.endcode == "2003":
            self.message = self.endcode + ": Table missing"
        elif self.endcode == "2004":
            self.message = self.endcode + ": Data missing"
        elif self.endcode == "2005":
            self.message = self.endcode + ": Program missing"
        elif self.endcode == "2006":
            self.message = self.endcode + ": File missing"
        elif self.endcode == "2007":
            self.message = self.endcode + ": Data mismatch"
        elif self.endcode == "2101":
            self.message = self.endcode + ": Read-only"
        elif self.endcode == "2102":
            self.message = self.endcode + ": Protected"
        elif self.endcode == "2103":
            self.message = self.endcode + ": Cannot register"
        elif self.endcode == "2105":
            self.message = self.endcode + ": Program missing"
        elif self.endcode == "2106":
            self.message = self.endcode + ": File missing"
        elif self.endcode == "2107":
            self.message = self.endcode + ": File name already exists"
        elif self.endcode == "2108":
            self.message = self.endcode + ": Cannot change"
        elif self.endcode == "2201":
            self.message = self.endcode + ": Not possible during execution"
        elif self.endcode == "2202":
            self.message = self.endcode + ": Not possible while running"
        elif self.endcode == "2203":
            self.message = self.endcode + ": Wrong PLC mode, PROGRAM mode"
        elif self.endcode == "2204":
            self.message = self.endcode + ": Wrong PLC mode, DEBUG mode"
        elif self.endcode == "2205":
            self.message = self.endcode + ": Wrong PLC mode, MONITOR mode"
        elif self.endcode == "2206":
            self.message = self.endcode + ": Wrong PLC mode, RUN mode"
        elif self.endcode == "2207":
            self.message = self.endcode + ": Specified node not polling node"
        elif self.endcode == "2208":
            self.message = self.endcode + ": Step cannot be executed"
        elif self.endcode == "2301":
            self.message = self.endcode + ": File device missing"
        elif self.endcode == "2302":
            self.message = self.endcode + ": Memory missing"
        elif self.endcode == "2303":
            self.message = self.endcode + ": Clock missing"
        elif self.endcode == "2401":
            self.message = self.endcode + ": Table missing"

        else:
            self.message = self.endcode

        self.message = "FINS ERROR " + self.message

    def __str__(self):
        return repr(self.message)


class fins:
    addr = ()
    destfins = []
    srcfins = []
    port = 9600
    

    def __init__(self, host, destfinsadr="0.0.0", srcfinsadr="0.1.0"):
        self.addr = host, self.port
        self.destfins = destfinsadr.split('.')
        if destfinsadr=="0.0.0":
            self.hostadr = host.split('.')
            self.destfins[1] = self.hostadr[3]

        self.srcfins = srcfinsadr.split('.')

    def offset(self, adr, offset):
        mtype = adr[:1]
        moffset =[]
        if mtype == 'D':
            mtype = 0x82
            moffset = list((int(adr[1:])+offset).to_bytes(2,'big'))
        elif mtype == 'E':
            bank = int(adr[1:2], 16)
            mtype = 0xA0 + bank
            moffset = list((int(adr[3:])+offset).to_bytes(2,'big'))
        elif mtype.isdigit():
            mtype = 0xB0
            moffset = list((int(adr)+offset).to_bytes(2,'big'))
        elif mtype == 'W':
            mtype = 0xB1
            moffset = list((int(adr[1:])+offset).to_bytes(2,'big'))
        elif mtype == 'H':
            mtype = 0xB2
            moffset = list((int(adr[1:])+offset).to_bytes(2,'big'))
        
        return mtype, moffset

    # Fins Header
    def finsheader(self):
        ary = bytearray(10)
        ary[0] = 0x80
        ary[1] = 0x00
        ary[2] = 0x02
        ary[3] = int(self.destfins[0])      # Destination NetNo
        ary[4] = int(self.destfins[1])      # Destination NodeNo
        ary[5] = int(self.destfins[2])      # Destination UnitNo
        ary[6] = int(self.srcfins[0])       # Source NetNo
        ary[7] = int(self.srcfins[1])       # Source NodeNo
        ary[8] = int(self.srcfins[2])       # Source UnitNo
        ary[9] = 0x00                       # SID

        return ary

    # Memory area read
    def read(self, memaddr, readsize):
        s = socket(AF_INET, SOCK_DGRAM)
        s.settimeout(2)

        finsFrame = self.finsheader()
        finsary = bytearray(8)

        readnum = readsize // 990
        remainder = readsize % 990

        data = bytes()
        for cnt in range(readnum + 1):
            memtype, memoffset = self.offset(memaddr, cnt * 990)
            if cnt == readnum:
                rsize = list(int(remainder).to_bytes(2,'big'))
            else:
                rsize = list(int(990).to_bytes(2,'big'))
                
            finsary[0] = 0x01
            finsary[1] = 0x01
            finsary[2] = memtype
            finsary[3] = memoffset[0]
            finsary[4] = memoffset[1]
            finsary[5] = 0x00
            finsary[6] = rsize[0]
            finsary[7] = rsize[1]

            finsFrame.extend(finsary)

            s.sendto(finsFrame, self.addr)
            readdata = s.recv(BUFSIZE)

            data += readdata[14:]
        
        s.close()

        if not(readdata[12] == 0 and readdata[13] == 0):
            raise(FinsResponseError(readdata[12:14]))

        return data
            
    # Memory area write
    def write(self, memaddr, writedata):
        if len(writedata) % 2 == 1:
            return
        writeWordSize = len(writedata) // 2
        
        s = socket(AF_INET, SOCK_DGRAM)
        s.settimeout(2)

        writenum = writeWordSize // 990
        remainder = writeWordSize % 990

        finsres = bytes()
        for cnt in range(writenum + 1):
            memtype, memoffset = self.offset(memaddr, cnt * 990)
            if cnt == writenum:
                size = remainder
            else:
                size = 990
                
            rsize = list(int(size).to_bytes(2,'big'))
            finsary = bytearray(8 + size * 2)

            finsary[0] = 0x01
            finsary[1] = 0x02
            finsary[2] = memtype
            finsary[3] = memoffset[0]
            finsary[4] = memoffset[1]
            finsary[5] = 0x00
            finsary[6] = rsize[0]
            finsary[7] = rsize[1]
            pos = cnt * 990 * 2
            finsary[8:] = writedata[pos: pos + size * 2]

            finsFrame = self.finsheader()
            finsFrame.extend(finsary)

            s.sendto(finsFrame, self.addr)
            rcv = s.recv(BUFSIZE)

            if not(rcv[12] == 0 and rcv[13] == 0):
                raise(FinsResponseError(rcv[12:14]))

        s.close()

        finsres = rcv[10:]

        return finsres

    # Memory area fill
    def fill(self, memaddr, size, writedata):
        memtype, memoffset = self.offset(memaddr, 0)
        
        finsary = bytearray(10)
        finsary[0] = 0x01
        finsary[1] = 0x03
        finsary[2] = memtype
        finsary[3] = memoffset[0]
        finsary[4] = memoffset[1]
        finsary[5] = 0x00
        finsary[6:8] = struct.pack('>H', size) 
        finsary[8:] = struct.pack(">H", writedata)

        rcv = finsudp.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Multiple memory area read
    def multiRead(self, memadr):
        wd = memadr.replace(' ', '').split(',')
        wdary = []
        if len(wd) > 0:
            for d in wd:
                memtype, memoffset = self.offset(d, 0)
                wdary.append(memtype)
                wdary.append(memoffset[0])
                wdary.append(memoffset[1])
                wdary.append(0x00)

        s = socket(AF_INET, SOCK_DGRAM)
        s.settimeout(2)

        finsFrame = self.finsheader()
        finsary = bytearray(2 + len(wdary))

        finsary[0] = 0x01
        finsary[1] = 0x04
        finsary[2:] = wdary

        finsFrame.extend(finsary)

        s.sendto(finsFrame, self.addr)
        readdata = s.recv(BUFSIZE)

        s.close()

        data = bytearray(len(wd) * 2)
        for pos in range(len(wd)):
            wpos = 14 + pos * 3
            wdata = readdata[wpos: wpos + 3]
            data[pos * 2] = wdata[1]
            data[pos * 2 + 1] = wdata[2]

        return data

    # Run
    def run(self, mode):
        finsary = bytearray(5)
        finsary[0] = 0x04
        finsary[1] = 0x01
        finsary[2] = 0xFF
        finsary[3] = 0xFF
        finsary[4] = mode

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Stop
    def stop(self):
        finsary = bytearray(4)
        finsary[0] = 0x04
        finsary[1] = 0x02
        finsary[2] = 0xFF
        finsary[3] = 0xFF

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Read cpu unit data
    def ReadUnitData(self):
        finsary = bytearray(3)
        finsary[0] = 0x05
        finsary[1] = 0x01
        finsary[2] = 0x00

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Read cpu unit status
    def ReadUnitStatus(self):
        finsary = bytearray(2)
        finsary[0] = 0x06
        finsary[1] = 0x01

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Read cycle time
    def ReadCycletime(self):
        finsary = bytearray(3)
        finsary[0] = 0x06
        finsary[1] = 0x20
        finsary[2] = 0x01

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Clock
    def Clock(self):
        finsary = bytearray(2)
        finsary[0] = 0x07
        finsary[1] = 0x01

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        if finsres[2] == 0x00 and finsres[3] == 0x00:
            dtAry = finsres[4:10]
            dtStr = dtAry.hex()
            PlcDateTime = datetime.strptime(dtStr, '%y%m%d%H%M%S')
        else:
            PlcDateTime = None

        return PlcDateTime

    # Set clock
    def SetClock(self, dt):
        dtStr = dt.strftime('%y%m%d%H%M%S')
        dtAry = bytes.fromhex(dtStr)

        finsary = bytearray(14)
        finsary[0] = 0x07
        finsary[1] = 0x02
        finsary[2:] = dtAry

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Error Clear
    def ErrorClear(self):
        finsary = bytearray(4)
        finsary[0] = 0x21
        finsary[1] = 0x01
        finsary[2] = 0xFF
        finsary[3] = 0xFF

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Error log read last10
    def ErrorLogRead(self):
        finsary = bytearray(6)
        finsary[0] = 0x21
        finsary[1] = 0x02
        finsary[2] = 0x00
        finsary[3] = 0x00
        finsary[4] = 0x00
        finsary[5] = 0x0A

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres

    # Error log clear
    def ErrorLogClear(self):
        finsary = bytearray(2)
        finsary[0] = 0x21
        finsary[1] = 0x03

        rcv = self.SendCommand(finsary)
        finsres = rcv[10:]

        return finsres


    # Send fins command 
    def SendCommand(self, FinsCommand):
        s = socket(AF_INET, SOCK_DGRAM)
        s.settimeout(2)

        finsFrame = self.finsheader() + FinsCommand

        s.sendto(finsFrame, self.addr)
        readdata = s.recv(BUFSIZE)

        return readdata


    def toBin(self, data):
        outdata = format(int.from_bytes(data, 'big'), 'b')

        return outdata

    def WordToBin(self, data):
        size = len(data) * 8
        strBin = format(int.from_bytes(data, 'big'), 'b')
        outdata = (('0' * (size)) + strBin) [-size:]

        return outdata

    def toInt16(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 2):
            tmpdata = arydata[idx:idx+2]
            outdata += (struct.unpack('>h',tmpdata))
        
        return outdata

    def toUInt16(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 2):
            tmpdata = arydata[idx:idx+2]
            outdata += (struct.unpack('>H',tmpdata))
        
        return outdata

    def toInt32_old(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 4):
            tmpdata = arydata[idx:idx+4]
            outdata += (struct.unpack('>i',tmpdata))
        
        return outdata

    def toInt32(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 4):
            tmpdata = arydata[idx:idx+4]
            tmpdata[0:2], tmpdata[2:4] = tmpdata[2:4], tmpdata[0:2]
            outdata += (struct.unpack('>i',tmpdata))

        return outdata

    def toUInt32(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 4):
            tmpdata = arydata[idx:idx+4]
            tmpdata[0:2], tmpdata[2:4] = tmpdata[2:4], tmpdata[0:2]
            outdata += (struct.unpack('>I',tmpdata))
        
        return outdata

    def toInt64(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 8):
            tmpdata = arydata[idx:idx+8]
            tmpdata[0:2],tmpdata[2:4],tmpdata[4:6],tmpdata[6:8] = tmpdata[6:8],tmpdata[4:6],tmpdata[2:4],tmpdata[0:2]
            outdata += (struct.unpack('>q',tmpdata))

        return outdata
        
    def toUInt64(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 8):
            tmpdata = arydata[idx:idx+8]
            tmpdata[0:2],tmpdata[2:4],tmpdata[4:6],tmpdata[6:8] = tmpdata[6:8],tmpdata[4:6],tmpdata[2:4],tmpdata[0:2]
            outdata += (struct.unpack('>Q',tmpdata))
        
        return outdata

    def toFloat(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 4):
            tmpdata = arydata[idx:idx+4]
            tmpdata[0:2], tmpdata[2:4] = tmpdata[2:4], tmpdata[0:2]
            outdata += (struct.unpack('>f', tmpdata))

        return outdata

    def toDouble(self, data):
        outdata = []
        arydata = bytearray(data)
        for idx in range(0, len(arydata), 8):
            tmpdata = arydata[idx:idx+8]
            tmpdata[0:2],tmpdata[2:4],tmpdata[4:6],tmpdata[6:8] = tmpdata[6:8],tmpdata[4:6],tmpdata[2:4],tmpdata[0:2]
            outdata += (struct.unpack('>d', tmpdata))

        return outdata

    def toString(self, data):
        outdata = data.decode("utf-8")
        return outdata


if __name__ == "__main__":
    # Sample
    try:
        finsudp = fins('192.168.0.16')

        data = finsudp.read('0', 1)
        print(finsudp.toBin(data))
        print(finsudp.WordToBin(data))
        print(list(finsudp.WordToBin(data)))

        data = finsudp.read('W0', 2)
        print(finsudp.toBin(data))
        print(finsudp.WordToBin(data))
        print(list(finsudp.WordToBin(data)))

        data = finsudp.read('H0', 4)
        print(finsudp.toBin(data))
        print(finsudp.WordToBin(data))
        print(list(finsudp.WordToBin(data)))

        data = finsudp.read('D1000', 1)
        print(finsudp.toBin(data))
        print(finsudp.WordToBin(data))
        print(list(finsudp.WordToBin(data)))

        data = finsudp.read('D1001', 1)
        print(finsudp.toInt16(data))

        data = finsudp.read('D1002', 2)
        print(finsudp.toInt32(data))

        data = finsudp.read('D1004', 4)
        print(finsudp.toInt64(data))

        data = finsudp.read('D1008', 1)
        print(finsudp.toUInt16(data))

        data = finsudp.read('D1009', 2)
        print(finsudp.toUInt32(data))

        data = finsudp.read('D1011', 4)
        print(finsudp.toUInt64(data))

        data = finsudp.read('D1015', 2)
        print(finsudp.toFloat(data))

        data = finsudp.read('D1017', 4)
        print(finsudp.toDouble(data))

        data = finsudp.read('D1021', 5)
        print(finsudp.toString(data))


        data = finsudp.read('D1100', 10)
        print(finsudp.toUInt16(data))

        rcv = finsudp.write('E0_0', data)
        print(rcv)

        l = list(range(1000))
        writedata = list()
        for num in range(1000):
            writedata.extend(list(int(l[num]).to_bytes(2,'big')))
        rcv = finsudp.write('D1000', writedata)
        print(rcv)

        rcv = finsudp.fill('E0_100', 10, 55)
        print(rcv)

        data = finsudp.multiRead('D1000, D1010, D1020')
        print(finsudp.toUInt16(data))

        rcv = finsudp.run(0x02)
        print(rcv)

        rcv = finsudp.stop()
        print(rcv)

        rcv = finsudp.ReadUnitData()
        print(rcv)

        rcv = finsudp.ReadUnitStatus()
        print(rcv)

        rcv = finsudp.ReadCycletime()
        print(rcv)

        rcv = finsudp.Clock()
        print(rcv)

        rcv = finsudp.SetClock(datetime.now())
        print(rcv)

        rcv = finsudp.ErrorClear()
        print(rcv)

        rcv = finsudp.ErrorLogRead()
        print(rcv)

        rcv = finsudp.ErrorLogClear()
        print(rcv)

        cmd = bytearray([0x05,0x01])
        rcv = finsudp.SendCommand(cmd)
        print(rcv)

    except FinsError as e:
        print(e)

    except Exception as e:
        print(e)