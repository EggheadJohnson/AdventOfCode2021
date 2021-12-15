import pprint
from collections import deque

pp = pprint.PrettyPrinter(indent=4)

class Board2D:
    def __init__(self, positions):
        self.board = [ list(map(int, list(line))) for line in positions]
    def printBoard(self, separator=''):
        boardMaxVal = max([max(line) for line in self.board])
        boardMaxLen = len(str(boardMaxVal))
        for line in self.board:
            print(separator.join(map(str, line)))
    def getPosition(self, position):
        return self.board[position[0]][position[1]]
    def setPosition(self, position, value):
        self.board[position[0]][position[1]] = value
    def isPositionInBoard(self, position):
        return position[0] >= 0 and position[0] < len(self.board) and position[1] >= 0 and position[1] < len(self.board[0])
    def getAdjacentPositions(self, position):
        return list(filter(self.isPositionInBoard, [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
        ]))
    def getLastPosition(self):
        return (len(self.board) - 1, len(self.board[len(self.board) - 1]) - 1)

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

def getShortestCurrentPath(shortestPathDict, seenButNotVisited):
    min = None
    for k in seenButNotVisited:
        if not min or shortestPathDict[k] < shortestPathDict[min]:
            min = k
    return min

def dijkstra(board, startingPosition, endingPosition):
    shortestPathDict = {
        startingPosition: 0
    }
    visited = set()
    seenButNotVisited = set([(0, 0)])

    shortestPathPos = startingPosition

    while True:
        pos = getShortestCurrentPath(shortestPathDict, seenButNotVisited)
        if pos == endingPosition:
            return shortestPathDict[pos]
        for p in board.getAdjacentPositions(pos):
            if p not in visited:
                seenButNotVisited.add(p)
            if p not in shortestPathDict or board.getPosition(p) + shortestPathDict[pos] < shortestPathDict[p]:
                shortestPathDict[p] = board.getPosition(p) + shortestPathDict[pos]
            if p not in visited and shortestPathDict[p] < shortestPathDict[shortestPathPos]:
                shortestPathPos = p
        seenButNotVisited.remove(pos)
        visited.add(pos)


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
