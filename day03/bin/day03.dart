import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;
import 'dart:math';

// run with, e.g., /usr/local/opt/dart/bin/dart bin/sample.dart -p

/**
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 1000 lines
 * Part A Solution: 4160394
 * Part B Solution: 4125600
 */

void main(List<String> arguments) async {
  var fileName = 'input/${get_file_name.getFileName(arguments)}';
  List lineList = await dart_util.openFile(fileName);

  print("Opened $fileName with ${lineList.length} lines");

  var partA = solvePartA(lineList);
  var partB = solvePartB(lineList);


  print("Part A Solution: $partA");
  print("Part B Solution: $partB");

}

List getSumsPerPosition(List lineList) {
  List result = [];

  for (var i = 0; i < lineList[0].length; i++) {
    result.add(0);
  }

  for (var line in lineList) {
    var split_line = line.split('').map((i) => i == '1' ? 1 : -1).toList();
    for (var i = 0; i < split_line.length; i++) {
      result[i] += split_line[i];
    }
  }

  return result;
}

List getGamma(List sumsPerPosition) {
  return sumsPerPosition.map((s) => s >= 0 ? 1 : 0).toList();
}

List getEpsilon(List sumsPerPosition) {
  return sumsPerPosition.map((s) => s >= 0 ? 0 : 1).toList();
}

int fromBinary(List binaryItems) {
  bool shouldPrint = false;
  int i = binaryItems.length - 1;
  int total = 0;
  for (var c in binaryItems) {
    total += (pow(2, i) * c).toInt();
    i--;
  }
  if (shouldPrint) print('input: $binaryItems output: $total');
  return total;
}

List getOxygenRating(List lineList) {
  var result = [];
  var pos = 0;

  while (lineList.length > 1 && pos < lineList[0].length) {
    var gamma = getGamma(getSumsPerPosition(lineList));
    lineList = lineList.where((l) => l.split('').map((i) => int.parse(i)).toList()[pos] == gamma[pos]).toList();
    pos += 1;
  }

  return lineList;
}

List getCO2ScrubberRating(List lineList) {
  var result = [];
  var pos = 0;

  while (lineList.length > 1 && pos < lineList[0].length) {
    var epsilon = getEpsilon(getSumsPerPosition(lineList));
    lineList = lineList.where((l) => l.split('').map((i) => int.parse(i)).toList()[pos] == epsilon[pos]).toList();
    pos += 1;
  }

  return lineList;
}

int solvePartA(List lineList) {
  var shouldPrint = false;
  var sumsPerPosition = getSumsPerPosition(lineList);
  if (shouldPrint) print(sumsPerPosition);
  var gamma = getGamma(sumsPerPosition);
  if (shouldPrint) print(gamma);
  var epsilon = getEpsilon(sumsPerPosition);
  if (shouldPrint) print(epsilon);
  var gamma_number = fromBinary(gamma);
  if (shouldPrint) print(gamma_number);
  var epsilon_number = fromBinary(epsilon);
  if (shouldPrint) print(epsilon_number);
  return gamma_number * epsilon_number;
}

int solvePartB(List lineList) {
  var shouldPrint = false;
  var oxygenRating = getOxygenRating(lineList);
  if (shouldPrint) print('oxygen: $oxygenRating');
  var co2Rating = getCO2ScrubberRating(lineList);
  if (shouldPrint) print('co2: $co2Rating');
  var oxygen_number = fromBinary(oxygenRating[0].split('').map((i) => int.parse(i)).toList());
  if (shouldPrint) print('o2 num: $oxygen_number');
  var co2_number = fromBinary(co2Rating[0].split('').map((i) => int.parse(i)).toList());
  if (shouldPrint) print('co2 num: $co2_number');

  return oxygen_number*co2_number;
}
