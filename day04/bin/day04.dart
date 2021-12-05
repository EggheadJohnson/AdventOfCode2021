import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;

// run with, e.g., /usr/local/opt/dart/bin/dart bin/sample.dart -p

/**
 * Opening input/puzzle.txt
 * Opened input/puzzle.txt with 601 lines
 * Part A Solution: 23177
 * Part B Solution: 6804
 */

void main(List<String> arguments) async {
  var fileName = 'input/${get_file_name.getFileName(arguments)}';
  List lineList = await dart_util.openFile(fileName);

  print("Opened $fileName with ${lineList.length} lines");
  var spots = lineList[0].split(',');
  var boards = parseAllBoards(lineList.sublist(2));

  var partA = solvePartA(spots, boards);
  boards = parseAllBoards(lineList.sublist(2));
  var partB = solvePartB(spots, boards);


  print("Part A Solution: $partA");
  print("Part B Solution: $partB");

}

bool shouldPrint() {
  return false;
}

Map parseBoard(List boardLines) {
  var split_lines = boardLines.map((line) => line.split(' ')).toList();
  var val_to_pos_map = {};
  for (var i = 0; i < split_lines.length; i++) {
    var line = split_lines[i];
    for (var j = 0; j < line.length; j++) {
      val_to_pos_map[split_lines[i][j]] = [ i, j ];
    }
  }
  return {
    'cols': [0, 0, 0, 0, 0,],
    'rows': [0, 0, 0, 0, 0,],
    'board': split_lines,
    'mapped': val_to_pos_map,
    'has_won': false,
  };
}

List parseAllBoards(List lineList) {
  List parsedBoards = [];
  List currLines = [];
  for (var line in lineList) {
    line = line.trim().replaceAll(RegExp(r'  '), ' ');
    if (line.length == 0) {
      var board = parseBoard(currLines);
      parsedBoards.add(board);
      currLines = [];
    } else {
      currLines.add(line);
    }
  }
  if (currLines.length != 0) {
    var board = parseBoard(currLines);
    parsedBoards.add(board);
  }
  return parsedBoards;
}

bool allUnique(List spots) {
  var spot_set = Set();
  for (var spot in spots) {
    if (spot_set.contains(spot)) {
      return false;
    }
    spot_set.add(spot);
  }
  return true;
}

List takeSingleStep(String spot, List boards) {
  for (var board in boards) {
    if (board['mapped'].containsKey(spot)) {
      var spot_pos = board['mapped'][spot];

      board['board'][spot_pos[0]][spot_pos[1]] = '.';
      board['cols'][spot_pos[1]] += 1;
      board['rows'][spot_pos[0]] += 1;

      if (board['cols'].contains(5) || board['rows'].contains(5)) board['has_won'] = true;
    }
  }
  return boards;
}

void printBoard(Map board) {
  print('~~~~~~~~~~~~~~~~~');
  for (var line in board['board']) {
    var board_line = '';
    for (var item in line) {
      if (item == '.' || int.parse(item) < 10) {
        board_line += ' ';
      }
      board_line += item + ' ';
    }
    print(board_line);

  }
  print('');
  print('cols: ${board['cols']}');
  print('rows: ${board['rows']}');
  print('has won: ${board['has_won']}');
  print('');
  print('~~~~~~~~~~~~~~~~~');
}

bool isThereAWinner(List boards) {
  for (var board in boards) {
    if (board['cols'].contains(5) || board['rows'].contains(5)) return true;
  }
  return false;
}

Map extractWinner(List boards) {
  for (var board in boards) {
    if (board['cols'].contains(5) || board['rows'].contains(5)) return board;
  }
  return {
    'error': 'No winner found',
  };
}

int calculateBoard(String spot, Map board) {
  var board_sum = 0;
  for (var line in board['board']) {
    for (var val in line) {
      if (val != '.') board_sum += int.parse(val);
    }
  }
  return int.parse(spot) * board_sum;
}

int solvePartA(List spots, List boards) {
  if (shouldPrint() && false) {
    print(spots);
    print(boards);

    for (var board in boards) {
      printBoard(board);
    }
  }

  var spot_ctr = -1;
  var spot;
  while (!isThereAWinner(boards)) {
    spot_ctr++;
    spot = spots[spot_ctr];
    boards = takeSingleStep(spot, boards);
  }

  var winning_board = extractWinner(boards);

  if (shouldPrint() && false) {
    printBoard(winning_board);
    print(spot);
  }

  return calculateBoard(spot, winning_board);
}

int solvePartB(List spots, List boards) {
  var spot_ctr = -1;
  var spot;
  while (boards.length > 1 || !boards[0]['has_won']) {
    spot_ctr++;
    spot = spots[spot_ctr];
    boards = takeSingleStep(spot, boards);
    if (boards.length > 1) boards.retainWhere((board) => !board['has_won']);
    if (shouldPrint()) {
      print(boards.length);
      printBoard(boards[0]);
    }
  }

  if (shouldPrint()) printBoard(boards[0]);

  return calculateBoard(spot, boards[0]);
}
