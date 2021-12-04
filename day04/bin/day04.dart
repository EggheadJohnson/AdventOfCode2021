import '../../dart_utils/lib/dart_utils.dart' as dart_util;
import '../../dart_utils/lib/get_file_name.dart' as get_file_name;

// run with, e.g., /usr/local/opt/dart/bin/dart bin/sample.dart -p

void main(List<String> arguments) async {
  var fileName = 'input/${get_file_name.getFileName(arguments)}';
  List lineList = await dart_util.openFile(fileName);

  print("Opened $fileName with ${lineList.length} lines");
  var spots = lineList[0].split(',');
  var boards = parseAllBoards(lineList.sublist(2));

  var partA = solvePartA(spots, boards);
  var partB = solvePartB(spots, boards);


  print("Part A Solution: $partA");
  print("Part B Solution: $partB");

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
    'diags': [0, 0,],
    'board': split_lines,
    'mapped': val_to_pos_map,
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
      if (spot_pos[0] == spot_pos[1]) {
        board['diags'][0] += 1;
      }
      if (spot_pos[0] + spot_pos[1] == 4) {
        board['diags'][1] += 1;
      }
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
  print('diags: ${board['diags']}');
  print('');
  print('~~~~~~~~~~~~~~~~~');
}

bool isThereAWinner(List boards) {
  for (var board in boards) {
    if (board['cols'].contains(5) || board['rows'].contains(5) || board['diags'].contains(5)) return true;
  }
  return false;
}

Map extractWinnter(List boards) {
  for (var board in boards) {
    if (board['cols'].contains(5) || board['rows'].contains(5) || board['diags'].contains(5)) return board;
  }
  return {
    'error': 'No winner found',
  };
}

int calculateBoard(String spot, Map board) {
  return board['board'].reduce((tot, val) => tot + val == '.' ? 0 : int.parse(val)) * int.parse(spot);
}

int solvePartA(List spots, List boards) {
  print(spots);
  print(boards);

  for (var board in boards) {
    printBoard(board);
  }

  boards = takeSingleStep(spots[0], boards);

  for (var board in boards) {
    printBoard(board);
  }

  return calculateBoard(boards[0]);
}

int solvePartB(List spots, List boards) {
  return -1;
}
