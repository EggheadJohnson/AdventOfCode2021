import pprint, sys
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra
from fromBinaryString import fromBinaryString

pp = pprint.PrettyPrinter(indent=4)

def parseInput(input):
    replacement = ''
    board = []
    replacementMode = True
    for line in input:
        if len(line) == 0:
            replacementMode = False
        elif replacementMode:
            replacement += line
        else:
            board.append(line)
    return replacement, board

def takeOneStep(board, replacement):
    output = []
    for i in range(1, len(board.board) - 1):
        newLine = ''
        for j in range(1, len(board.board[i]) - 1):
            ninePositions = board.getNineSpotsCenteredAtPos((i, j))
            nineValues = ''.join(list(map(lambda x: board.getPosition(x), ninePositions)))
            newLine += replacement[fromBinaryString(nineValues, '.', '#')]
        output.append(newLine)

    outputBoard = Board2D(output)
    outputBoard.padBoard(outputBoard.getPosition((0, 0)))
    return outputBoard



def part1(input):
    replacement, board = parseInput(input)
    board = Board2D(board)
    for x in range(3):
        board.padBoard('.')

    board = takeOneStep(board, replacement)
    for x in range(3):
        board.padBoard(board.getPosition((0, 0)))
    board = takeOneStep(board, replacement)
    return sum([ sum([ 1 if i == '#' else 0 for i in line ]) for line in board.board    ])

def part2(input):
    replacement, board = parseInput(input)
    board = Board2D(board)
    for x in range(3):
        board.padBoard('.')

    for x in range(50):
        board = takeOneStep(board, replacement)
        for x in range(3):
            board.padBoard(board.getPosition((0, 0)))
    return sum([ sum([ 1 if i == '#' else 0 for i in line ]) for line in board.board    ])
