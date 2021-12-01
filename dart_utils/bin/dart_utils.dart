import 'dart:io';
import 'dart:convert';
import 'dart:async';

Future<List> openFile(String fileName) async {
  print("Opening $fileName");
  final file = File(fileName);
  Stream<String> lines = file.openRead()
    .transform(utf8.decoder)       // Decode bytes to UTF-8.
    .transform(LineSplitter());    // Convert stream to individual lines.
  try {
    var lineList = [];
    await for (var line in lines) {
      lineList.add(line);
    }
    return lineList;
  } catch (e) {
    print('Error: $e');
    return [];
  }
}
