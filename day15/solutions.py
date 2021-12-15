import pprint, sys
from collections import deque
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

def parseInput(input):
    return [ list(map(int, line)) for line in input ]

def getLowestNeighbor(spot, square):
    up = (spot[0] - 1, spot[1])
    lt = (spot[0], spot[1] - 1)
    if up[0] < 0:
        return square[lt[0]][lt[1]]
    if lt[1] < 0:
        return square[up[0]][up[1]]
    return min(square[lt[0]][lt[1]], square[up[0]][up[1]])

def fillInSquare(square):
    spot = (0, 0)
    queue = deque([(1, 0), (0, 1)])
    visited = set([(0, 0), (1, 0), (0, 1)])
    square[0][0] = 0

    while queue:
        spot = queue.popleft()
        visited.add(spot)
        square[spot[0]][spot[1]] = square[spot[0]][spot[1]] + getLowestNeighbor(spot, square)
        if spot[0] < len(square) - 1 and (spot[0] + 1, spot[1]) not in visited:
            queue.append((spot[0] + 1, spot[1]))
            visited.add((spot[0] + 1, spot[1]))
        if spot[1] < len(square[0]) - 1 and (spot[0], spot[1] + 1) not in visited:
            queue.append((spot[0], spot[1] + 1))
            visited.add((spot[0], spot[1] + 1))
    return square

def buildMultiMap(input):
    output = []
    for y in range(5):
        for inputRow in input:
            outputRow = []
            for x in range(5):
                outputRow.extend( [ i + x + y - 9 if i + x + y > 9 else i + x + y for i in inputRow ] )
            output.append(outputRow)
    return output

def part1(input):
    square = parseInput(input)
    square = fillInSquare(square)
    board = Board2D(parseInput(input))
    return square[-1][-1]

def part2(input):
    square = parseInput(input)
    square = buildMultiMap(square)

    board = Board2D(square)
    return dijkstra(board, (0, 0), (len(board.board) - 1, len(board.board[len(board.board) - 1]) - 1))
