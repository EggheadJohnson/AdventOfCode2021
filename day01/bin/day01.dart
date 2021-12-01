import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;

void main(List<String> arguments) async {
  var fileName = 'input/${get_file_name.getFileName(arguments)}';
  List lineList = await dart_util.openFile(fileName);

  print("Opened $fileName with ${lineList.length} lines");

  var partA = solvePartA(lineList);
  var partB = solvePartB(lineList);


  print("Part A Solution: $partA");
  print("Part B Solution: $partB");

}

int solvePartA(List lineList) {
  return -1;
}

int solvePartB(List lineList) {
  return -1;
}
