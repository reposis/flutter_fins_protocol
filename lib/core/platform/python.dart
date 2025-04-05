import 'dart:io';
import 'package:flutter_fins_protocol/core/constant/files.dart';
import 'package:flutter_fins_protocol/core/platform/shell_script.dart';
import 'package:flutter/cupertino.dart';
import 'package:process_run/utils/process_result_extension.dart';

class Python {
  Python._();

  static Future<bool> installScript() async {
    bool pythonIsInstalled = await _checkPython3Installed();
    if (!pythonIsInstalled) {
      debugPrint(
          "Python3 is not installed. Install Python3 to use the library.");
      return false;
    }
    bool scriptCopied = await Files.exists(["fins.py", "fins_bridge.py"]);
    return scriptCopied || await _copyPythonScript();
  }

  static Future<bool> _checkPython3Installed() async {
    List<ProcessResult> result = await ShellScript.runCommand('python3 -V');
    return result.outText.startsWith("Python 3");
  }

  static Future<bool> _copyPythonScript() async {
    await Files.copyFromAssets("assets/script/fins.py", "fins.py");
    await Files.copyFromAssets(
        "assets/script/fins_bridge.py", "fins_bridge.py");

    return await Files.exists(["fins.py", "fins_bridge.py"]);
  }
}
