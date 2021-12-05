import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;

// run with, e.g., /usr/local/opt/dart/bin/dart bin/sample.dart -p

/**
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 500 lines
 * Part A Solution: 7436
 * Part B Solution: 21104
 */

/**
 * ➜  day05 git:(main) ✗ time dart bin/day05.dart -p (both approaches)
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 500 lines
 * Part A Solution: 7436
 * Part A second approach: 7436
 * Part B Solution: 21104
 * Part B second approach: 21104
 * dart bin/day05.dart -p  0.40s user 0.06s system 131% cpu 0.351 total
 * ➜  day05 git:(main) ✗ time dart bin/day05.dart -p (just the first approach)
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 500 lines
 * Part A Solution: 7436
 * Part B Solution: 21104
 * dart bin/day05.dart -p  0.21s user 0.08s system 133% cpu 0.222 total
 * ➜  day05 git:(main) ✗ time dart bin/day05.dart -p (just the second approach)
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 500 lines
 * Part A second approach: 7436
 * Part B second approach: 21104
 * dart bin/day05.dart -p  0.38s user 0.08s system 128% cpu 0.356 total
 */

void main(List<String> arguments) async {
  var fileName = 'input/${get_file_name.getFileName(arguments)}';
  List lineList = await dart_util.openFile(fileName);

  print("Opened $fileName with ${lineList.length} lines");

  var partA = solvePartA(lineList);
  var partB = solvePartB(lineList);

  // print("Part A Solution: $partA");
  print("Part A second approach: ${secondApproachForA(lineList)}");
  // print("Part B Solution: $partB");
  print("Part B second approach: ${secondApproachForB(lineList)}");

}

List processLines(List lineList) {
  return lineList.map((line) => line.split(' -> ').map((pair) => pair.split(',').map((i) => int.parse(i)).toList()).toList()).toList();
}

bool isHorizVert(List pair) {
  return pair[0][0] == pair[1][0] || pair[0][1] == pair[1][1];
}

int findMaxesAndMins(List pairList) {
  bool shouldPrint = false;
  var minCol = 10000; // They seem to all be under 10k, if we get back 10k, inrease this
  var maxCol = 0;
  var minRow = 10000; // They seem to all be under 10k, if we get back 10k, inrease this
  var maxRow = 0;

  for (var startEndPair in pairList) {
    for (var pair in startEndPair) {
      if (pair[0] < minCol) minCol = pair[0];
      if (pair[0] > maxCol) maxCol = pair[0];
      if (pair[1] < minRow) minRow = pair[1];
      if (pair[1] > maxRow) maxRow = pair[1];
    }
  }
  if (shouldPrint) print('Columns: $minCol - $maxCol');
  if (shouldPrint) print('Rows:    $minRow - $maxRow');
  return maxRow > maxCol ? maxRow : maxCol;
}

List buildBlankBoard([var size=1000]) {
  var board = [];
  for (var i = 0; i < size; i++) {
    var line = [];
    for (var j = 0; j < size; j++) {
      line.add(0);
    }
    board.add(line);
  }
  return board;
}

List getPairSlope(List pair) {
  var horiz, vert;
  if (pair[1][0] == pair[0][0]) horiz = 0;
  else horiz = pair[1][0] > pair[0][0] ? 1 : -1;
  if (pair[1][1] == pair[0][1]) vert = 0;
  else vert = pair[1][1] > pair[0][1] ? 1 : -1;
  return [horiz, vert];
}

List fillInBoard(List board, List pairs) {
  for (var pair in pairs) {
    var slope = getPairSlope(pair);
    var pos = pair[0];
    while (!(pos[0] == pair[1][0] && pos[1] == pair[1][1])) {
      board[pos[0]][pos[1]]++;
      pos[0] += slope[0];
      pos[1] += slope[1];
    }
    board[pos[0]][pos[1]]++;
  }
  return board;
}

void printBoard(List board) {
  for (var line in board) {
    print(line);
  }
}
int countOverlaps(List board) {
  var tot = 0;
  for (var line in board) {
    for (var i in line) {
      tot += i > 1 ? 1 : 0;
    }
  }
  return tot;
}
int solvePartA(List lineList) {
  var pairs = processLines(lineList);
  pairs.retainWhere((pair) => isHorizVert(pair));
  var board = buildBlankBoard(findMaxesAndMins(pairs) + 1);
  board = fillInBoard(board, pairs);
  return countOverlaps(board);
}

int solvePartB(List lineList) {
  var pairs = processLines(lineList);
  var board = buildBlankBoard(findMaxesAndMins(pairs) + 1);
  board = fillInBoard(board, pairs);
  return countOverlaps(board);
}

List fillInSpots(List pair) {
  var slope = getPairSlope(pair);
  var pos = pair[0];
  List spots = [];
  while (!(pos[0] == pair[1][0] && pos[1] == pair[1][1])) {
    spots.add(pos.join(','));
    pos[0] += slope[0];
    pos[1] += slope[1];
  }
  spots.add(pos.join(','));
  return spots;
}

int secondApproachForA(List lineList) {
  var pairs = processLines(lineList);
  pairs.retainWhere((pair) => isHorizVert(pair));
  Map spots = {};
  for (var pair in pairs) {
    var pair_spots = fillInSpots(pair);
    for (var spot in pair_spots) {
      if (!spots.containsKey(spot)) {
        spots[spot] = 0;
      }
      spots[spot]++;
    }
  }
  int total = 0;
  spots.forEach((key, val) {
    if (val > 1) total++;
  });
  return total;
}

int secondApproachForB(List lineList) {
  var pairs = processLines(lineList);
  Map spots = {};
  for (var pair in pairs) {
    var pair_spots = fillInSpots(pair);
    for (var spot in pair_spots) {
      if (!spots.containsKey(spot)) {
        spots[spot] = 0;
      }
      spots[spot]++;
    }
  }
  int total = 0;
  spots.forEach((key, val) {
    if (val > 1) total++;
  });
  return total;
}
