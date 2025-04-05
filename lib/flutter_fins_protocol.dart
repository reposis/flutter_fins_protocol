library flutter_fins_protocol;

import 'dart:io';

import 'package:flutter_fins_protocol/core/platform/shell_script.dart';
import 'package:flutter_fins_protocol/core/type/memory_areas.dart';
import 'package:flutter_fins_protocol/core/type/run_modes.dart';
import 'package:process_run/process_run.dart';

import 'core/type/commands.dart';

part 'core/command/fins_command.dart';

part 'core/implement/fins_protocol_dynamic.dart';
part 'core/implement/fins_protocol_static.dart';

abstract class FlutterFinsProtocol {
  static FinsProtocolStatic staticIp(String ip) => _FinsProtocolStatic._().setIp(ip);

  static FinsProtocolDynamic dynamicIp() => _FinsProtocolDynamic._();
}

class _FinsProtocolStatic extends FinsProtocolStatic {
  late String _ip;
  late _FinsCommand _command;

  _FinsProtocolStatic._();

  _FinsProtocolStatic setIp(String ip) {
    _command = _FinsCommand();
    _ip = ip;
    return this;
  }

  @override
  Future<String> write(MemoryAreas area, int offset, List<int> data,
      [int? bit]) async {
    String cmd = _command.write(_ip, area, offset, data);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> read(MemoryAreas area, int offset, int size,
      [int? bit]) async {
    String cmd = _command.read(_ip, area, offset, size);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> multiRead(List<String> dataAddresses) async {
    String cmd = _command.multiRead(_ip, dataAddresses);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> stop() async {
    String cmd = _command.stop(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> run(RunModes runMode) async {
    String cmd = _command.run(_ip, runMode);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> readUnitStatus() async {
    String cmd = _command.readUnitStatus(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> readUnitData() async {
    String cmd = _command.readUnitData(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> readCycleTime() async {
    String cmd = _command.readCycleTime(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> clock() async {
    String cmd = _command.clock(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> updateClock() async {
    String cmd = _command.updateClock(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> errorLogRead() async {
    String cmd = _command.errorLogRead(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> errorLogClear() async {
    String cmd = _command.errorLogClear(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> errorClear() async {
    String cmd = _command.errorClear(_ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> sendCommand(String command) async {
    String cmd = _command.sendCommand(_ip, command);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<int?> ping() async {
    try {
      int startMillis = DateTime.now().millisecondsSinceEpoch;
      var result = await read(MemoryAreas.DM, 2, 1);
      if (result.isEmpty) {
        return null;
      }
      int endMillis = DateTime.now().millisecondsSinceEpoch;
      return endMillis - startMillis;
    } catch (_) {}
    return null;
  }
}

class _FinsProtocolDynamic extends FinsProtocolDynamic {
  static final _FinsCommand _command = _FinsCommand();

  _FinsProtocolDynamic._();

  @override
  Future<String> write(String ip, MemoryAreas area, int offset, List<int> data,
      [int? bit]) async {
    String cmd = _command.write(ip, area, offset, data);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> read(String ip, MemoryAreas area, int offset, int size,
      [int? bit]) async {
    String cmd = _command.read(ip, area, offset, size);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> multiRead(String ip, List<String> dataAddresses) async {
    String cmd = _command.multiRead(ip, dataAddresses);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> stop(String ip) async {
    String cmd = _command.stop(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> run(String ip, RunModes runMode) async {
    String cmd = _command.run(ip, runMode);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> readUnitStatus(String ip) async {
    String cmd = _command.readUnitStatus(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> readUnitData(String ip) async {
    String cmd = _command.readUnitData(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> readCycleTime(String ip) async {
    String cmd = _command.readCycleTime(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> clock(String ip) async {
    String cmd = _command.clock(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> updateClock(String ip) async {
    String cmd = _command.updateClock(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> errorLogRead(String ip) async {
    String cmd = _command.errorLogRead(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> errorLogClear(String ip) async {
    String cmd = _command.errorLogClear(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> errorClear(String ip) async {
    String cmd = _command.errorClear(ip);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<String> sendCommand(String ip, String command) async {
    String cmd = _command.sendCommand(ip, command);
    List<ProcessResult> result = await ShellScript.runCommand(cmd);
    return result.outText;
  }

  @override
  Future<int?> ping(String ip) async {
    try {
      int startMillis = DateTime.now().millisecondsSinceEpoch;
      var result = await read(ip, MemoryAreas.DM, 2, 1);
      if (result.isEmpty) {
        return null;
      }
      int endMillis = DateTime.now().millisecondsSinceEpoch;
      return endMillis - startMillis;
    } catch (_) {}
    return null;
  }
}
