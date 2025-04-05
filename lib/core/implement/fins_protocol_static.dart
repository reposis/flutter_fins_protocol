part of '../../flutter_fins_protocol.dart';

abstract class FinsProtocolStatic{

  Future<String> write(MemoryAreas area, int offset, List<int> data, [int? bit]);

  Future<String> read(MemoryAreas area, int offset, int size, [int? bit]);

  Future<int?> ping();

  Future<String> multiRead(List<String> dataAddresses);

  Future<String> stop();

  Future<String> run(RunModes runMode);

  Future<String> readUnitStatus();

  Future<String> readUnitData();

  Future<String> readCycleTime();

  Future<String> clock();

  Future<String> updateClock();

  Future<String> errorLogRead();

  Future<String> errorLogClear();

  Future<String> errorClear();

  Future<String> sendCommand(String cmd);
}