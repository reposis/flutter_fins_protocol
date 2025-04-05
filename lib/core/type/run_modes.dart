enum RunModes{
  monitor,
  run
}
extension RunModesExtension on RunModes {
  String get value {
    switch (this) {
      case RunModes.monitor:
        return '2';
      default:
        return '4';
    }
  }
}