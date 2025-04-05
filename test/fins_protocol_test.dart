import 'package:flutter_fins_protocol/core/platform/python.dart';
import 'package:flutter_fins_protocol/core/type/memory_areas.dart' show MemoryAreas;
import 'package:flutter_fins_protocol/core/type/run_modes.dart';
import 'package:flutter_fins_protocol/flutter_fins_protocol.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('write', () async {
    FinsProtocolDynamic fins = FlutterFinsProtocol.dynamicIp();
    print(await fins.write("192.168.250.20", MemoryAreas.DM, 100, [0, 4], 01));
  }, skip: true);

  test('read', () async {
    FinsProtocolStatic fins = FlutterFinsProtocol.staticIp("192.168.250.20");
    String all = await fins.read(MemoryAreas.DM, 100, 989);
    print(all);
    print(await fins.read(MemoryAreas.HOLDING_BIT, 10, 1));
  }, skip: true);

  test('ping', () async {
    FinsProtocolDynamic fins = FlutterFinsProtocol.dynamicIp();
    print(await fins.ping("192.168.250.20"));
  }, skip: true);

  test('multiRead', () async {
    print(await FlutterFinsProtocol.dynamicIp()
        .multiRead("192.168.250.20", ["D100", "H10_1"]));
  }, skip: true);

  test('stop', () async {
    print(await FlutterFinsProtocol.dynamicIp().stop("192.168.250.20"));
  }, skip: true);

  test('run', () async {
    print(await FlutterFinsProtocol.dynamicIp().run("192.168.250.20", RunModes.run));
  }, skip: true);

  test('read_unit_status', () async {
    print(await FlutterFinsProtocol.dynamicIp().readUnitStatus("192.168.250.20"));
  }, skip: true);

  test('read_unit_data', () async {
    print(await FlutterFinsProtocol.dynamicIp().readUnitData("192.168.250.20"));
  }, skip: true);

  test('read_cycle_time', () async {
    print(await FlutterFinsProtocol.dynamicIp().readCycleTime("192.168.250.20"));
  }, skip: true);

  test('clock', () async {
    print(await FlutterFinsProtocol.dynamicIp().clock("192.168.250.20"));
  }, skip: true);

  test('update_clock', () async {
    print(await FlutterFinsProtocol.dynamicIp().updateClock("192.168.250.20"));
  }, skip: true);

  test('error_log_read', () async {
    print(await FlutterFinsProtocol.dynamicIp().errorLogRead("192.168.250.20"));
  }, skip: true);

  test('error_log_clear', () async {
    print(await FlutterFinsProtocol.dynamicIp().errorLogClear("192.168.250.20"));
  }, skip: true);

  test('error_clear', () async {
    print(await FlutterFinsProtocol.dynamicIp().errorClear("192.168.250.20"));
  }, skip: true);

  test('send_command', () async {
    print(
        await FlutterFinsProtocol.dynamicIp().sendCommand("192.168.250.20", "[4,1]"));
  }, skip: true);

  test('install python script', () async {
    WidgetsFlutterBinding.ensureInitialized();
    print(await Python.installScript());
  }, skip: true);
}
