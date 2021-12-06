import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;

// run with, e.g., /usr/local/opt/dart/bin/dart bin/sample.dart -p

/**
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 1 lines
 * Part A Solution: 366057
 * Part B Solution: 1653559299811
 */

void main(List<String> arguments) async {
  var fileName = 'input/${get_file_name.getFileName(arguments)}';
  List lineList = await dart_util.openFile(fileName);
  List fish = lineList[0].split(',').map((i) => int.parse(i)).toList();

  print("Opened $fileName with ${lineList.length} lines");

  var partA = solvePartA(fish);
  var partB = solvePartB(fish);


  print("Part A Solution: $partA");
  print("Part B Solution: $partB");

}

List<int> takeStep(fishList) {
  int today = fishList[0];
  fishList = fishList.sublist(1);
  fishList[6] += today;
  fishList.add(today);
  return fishList;
}

List<int> runPuzzle(List<int> fishList, [int days = 80]) {
  for (var i = 0; i < days; i++) {
    fishList = takeStep(fishList);
  }
  return fishList;
}

int solvePartA(List lineList) {
  List<int> fishList = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ];
  for (int fish in lineList) {
    fishList[fish] += 1;
  }

  fishList = runPuzzle(fishList, 80);

  return fishList.reduce((tot, val) => tot+val);
}

int solvePartB(List lineList) {
  List<int> fishList = [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ];
  for (int fish in lineList) {
    fishList[fish] += 1;
  }

  fishList = runPuzzle(fishList, 256);

  return fishList.reduce((tot, val) => tot+val);
}
