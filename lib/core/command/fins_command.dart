part of '../../flutter_fins_protocol.dart';

class _FinsCommand {

  String write(String ip, MemoryAreas area, int offset, List<int> data, [int? bit]){
    return _generateCommand(ip, Commands.write, ["${area.value}$offset${bit != null ? "_$bit" : ""}", data.toString().replaceAll(" ", "")]);
  }

  String read(String ip, MemoryAreas area, int offset, int size, [int? bit]){
    return _generateCommand(ip, Commands.read, ["${area.value}$offset${bit != null ? "_$bit" : ""}", size.toString()]);
  }

  String multiRead(String ip, List<String> dataAddresses){
    return _generateCommand(ip, Commands.multi_read, [dataAddresses.reduce((a,b)=>"$a,$b")]);
  }

  String stop(String ip){
    return _generateCommand(ip, Commands.stop, []);
  }

  String run(String ip, RunModes runMode){
    return _generateCommand(ip, Commands.run, [runMode.value]);
  }

  String readUnitStatus(String ip){
    return _generateCommand(ip, Commands.read_unit_status, []);
  }

  String readUnitData(String ip){
    return _generateCommand(ip, Commands.read_unit_data, []);
  }

  String readCycleTime(String ip){
    return _generateCommand(ip, Commands.read_cycle_time, []);
  }

  String clock(String ip){
    return _generateCommand(ip, Commands.clock, []);
  }

  String updateClock(String ip){
    return _generateCommand(ip, Commands.update_clock, []);
  }

  String errorLogRead(String ip){
    return _generateCommand(ip, Commands.error_log_read, []);
  }

  String errorLogClear(String ip){
    return _generateCommand(ip, Commands.error_log_clear, []);
  }

  String errorClear(String ip){
    return _generateCommand(ip, Commands.error_clear, []);
  }

  String sendCommand(String ip,String cmd){
    return _generateCommand(ip, Commands.send_command, [cmd]);
  }

  String _generateCommand(String ip, Commands command,
      List<String> args) {
    return "python3 fins_bridge.py $ip ${command.name}${args.isNotEmpty ? " ${args.reduce((a,
        b) => "$a $b")}":""}";
  }
}