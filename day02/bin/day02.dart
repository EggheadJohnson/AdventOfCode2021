import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;

/**
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 1000 lines
 * Part A Solution: 1936494
 * Part B Solution: 1997106066
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

Map move(Map pos, String line) {
  var splitLine = line.split(' ');
  var direction = splitLine[0];
  var distance = int.parse(splitLine[1]);
  switch (direction) {
    case 'forward':
      pos['horiz'] += distance;
      break;
    case 'up':
      pos['vert'] -= distance;
      break;
    case 'down':
      pos['vert'] += distance;
      break;
    default:
      print("PANIC UNRECOGNIZED DIRECTION: $direction");

  }
  return pos;
}

Map moveB(Map pos, String line) {
  var splitLine = line.split(' ');
  var direction = splitLine[0];
  var distance = int.parse(splitLine[1]);
  switch (direction) {
    case 'forward':
      pos['horiz'] += distance;
      pos['vert'] += distance * pos['aim'];
      break;
    case 'up':
      pos['aim'] -= distance;
      break;
    case 'down':
      pos['aim'] += distance;
      break;
    default:
      print("PANIC UNRECOGNIZED DIRECTION: $direction");

  }
  return pos;
}

int solvePartA(List lineList) {
  Map pos = {
    'horiz': 0,
    'vert': 0,
  };

  for (var line in lineList) {
    pos = move(pos, line);
  }

  return pos['horiz']*pos['vert'];
}

int solvePartB(List lineList) {
  Map pos = {
    'horiz': 0,
    'vert': 0,
    'aim': 0,
  };

  for (var line in lineList) {
    pos = moveB(pos, line);
  }

  return pos['horiz']*pos['vert'];
}
