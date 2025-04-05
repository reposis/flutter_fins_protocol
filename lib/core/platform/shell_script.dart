import 'dart:io';
import 'package:process_run/process_run.dart';

class ShellScript{
  ShellScript._();
  static Future<List<ProcessResult>> runCommand(
      String cmd) async {
    List<ProcessResult> results = [];
    try {
      var shell = Shell(
          options:
          ShellOptions(verbose: false, runInShell: true));
      results = await shell.run(cmd);
    } catch (_) {}
    return results;
  }
}