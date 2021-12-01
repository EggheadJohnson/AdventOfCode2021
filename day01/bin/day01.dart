import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;

/**
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 2000 lines
 * Part A Solution: 1713
 * Part B Solution: 1734
 */

void main(List<String> arguments) async {
  var fileName = 'input/${get_file_name.getFileName(arguments)}';
  List lineList = await dart_util.openFile(fileName);
  List<int> parsedLines = lineList.map((i) => int.parse(i)).toList();

  print("Opened $fileName with ${lineList.length} lines");

  var partA = solvePartA(parsedLines);
  var partB = solvePartB(parsedLines);


  print("Part A Solution: $partA");
  print("Part B Solution: $partB");

}

int solvePartA(List lineList) {
  int count = 0;
  for (var i = 1; i < lineList.length; i++) {
    if (lineList[i] > lineList[i - 1] ) {
      count++;
    }
  }
  return count;
}

List parseToSums(List<int> lineList) {
  List result = [];

  for (var i = 0; i < lineList.length - 2; i++) {
    result.add(lineList.sublist(i, i+3).reduce((tot, val) => tot+val));
  }

  return result;
}

int solvePartB(List<int> lineList) {
  return solvePartA(parseToSums(lineList));
}
