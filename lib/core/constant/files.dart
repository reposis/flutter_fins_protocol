import 'dart:io';

import 'package:flutter/services.dart';

class Files{
  Files._();

  static Future<void> copyFromAssets(
      String assetsPath, String destinationPath) async {
    ByteData data = await rootBundle.load(assetsPath);
    List<int> bytes =
    data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes);

    String path = destinationPath;
    if (File(path).existsSync()) {
      File(path).deleteSync();
    }
    await File(path).create();
    await File(path).writeAsBytes(bytes);
  }

  static bool existsSync(List<String> paths) {
    bool anyNotExist = false;
    for(String path in paths) {
      if(!File(path).existsSync()){
        anyNotExist = true;
      }
    }
    return anyNotExist;
  }

  static Future<bool> exists(List<String> paths) async {
    bool anyNotExists = false;
    for(String path in paths) {
      bool exists = await File(path).exists();
      if(!exists){
        anyNotExists = true;
      }
    }
    return !anyNotExists;
  }
}