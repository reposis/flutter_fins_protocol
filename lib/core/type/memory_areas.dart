enum MemoryAreas{
  DM,
  EM,
  WORK,
  HOLDING_BIT
}
extension MemoryAreasExtension on MemoryAreas {
  String get value {
    switch (this) {
      case MemoryAreas.DM:
        return 'D';
      case MemoryAreas.EM:
        return 'E';
      case MemoryAreas.WORK:
        return 'W';
      case MemoryAreas.HOLDING_BIT:
        return 'H';
      default:
        return '';
    }
  }
}