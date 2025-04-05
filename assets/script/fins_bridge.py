from fins import fins
from datetime import datetime
import time
import sys
import json

argumentList = sys.argv[1:]
if len(argumentList) < 1:
    print("destination ip required")
else:
    finsudp = fins(argumentList[0])

if len(argumentList) == 4 and argumentList[1] == "write":
    rec = finsudp.write(argumentList[2],json.loads(argumentList[3]))
    print(rec)
elif len(argumentList) == 4 and argumentList[1] == "read":
    rec = finsudp.read(argumentList[2],json.loads(argumentList[3]))
    print(finsudp.toInt16(rec))
elif len(argumentList) == 3 and argumentList[1] == "multi_read":
    rec = finsudp.multiRead(argumentList[2])
    print(finsudp.toInt16(rec))
elif len(argumentList) == 2 and argumentList[1] == "stop":
    rec = finsudp.stop()
    print(finsudp.toInt32(rec))
elif len(argumentList) == 3 and argumentList[1] == "run":
    rec = finsudp.run(int(argumentList[2]))
    print(finsudp.toInt32(rec))
elif len(argumentList) == 2 and argumentList[1] == "read_unit_data":
    rec = finsudp.ReadUnitData()
    print(rec)
elif len(argumentList) == 2 and argumentList[1] == "read_unit_status":
    rec = finsudp.ReadUnitStatus()
    print(rec)
elif len(argumentList) == 2 and argumentList[1] == "read_cycle_time":
    rec = finsudp.ReadCycletime()
    print(rec)
elif len(argumentList) == 2 and argumentList[1] == "clock":
    rec = finsudp.Clock()
    print(rec)
elif len(argumentList) == 2 and argumentList[1] == "update_clock":
    rec = finsudp.SetClock(datetime.now())
    print(rec)
elif len(argumentList) == 2 and argumentList[1] == "error_clear":
    rec = finsudp.ErrorClear()
    print(rec)
elif len(argumentList) == 2 and argumentList[1] == "error_log_read":
    rec = finsudp.ErrorLogRead()
    print(rec)
elif len(argumentList) == 2 and argumentList[1] == "error_log_clear":
    rec = finsudp.ErrorLogClear()
    print(rec)
elif len(argumentList) == 3 and argumentList[1] == "send_command":
    cmd = bytearray(json.loads(argumentList[2]))
    rec = finsudp.SendCommand(cmd)
    print(rec)
