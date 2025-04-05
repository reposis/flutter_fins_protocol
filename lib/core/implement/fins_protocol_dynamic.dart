part of '../../flutter_fins_protocol.dart';

abstract class FinsProtocolDynamic{

  Future<String> write(String ip, MemoryAreas area, int offset, List<int> data, [int? bit]);

  Future<String> read(String ip, MemoryAreas area, int offset, int size, [int? bit]);

  Future<int?> ping(String ip);

  Future<String> multiRead(String ip, List<String> dataAddresses);

  Future<String> stop(String ip);

  Future<String> run(String ip, RunModes runMode);

  Future<String> readUnitStatus(String ip);

  Future<String> readUnitData(String ip);

  Future<String> readCycleTime(String ip);

  Future<String> clock(String ip);

  Future<String> updateClock(String ip);

  Future<String> errorLogRead(String ip);

  Future<String> errorLogClear(String ip);

  Future<String> errorClear(String ip);

  Future<String> sendCommand(String ip,String cmd);
}