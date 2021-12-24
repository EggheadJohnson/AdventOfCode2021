import pprint, sys, itertools
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

def buildEmptyBoard(size=101):
    board = []
    for x in range(size):
        plane = []
        for y in range(size):
            line = []
            for z in range(size):
                line.append('.') # off
            plane.append(line)
        board.append(plane)
    return board

def setBoardPosition(board, pos, state):
    board[pos[0]+50][pos[1]+50][pos[2]+50] = state
    return board

def parseInput(input):
    parsed = []
    for line in input:
        state, positions = line.split(' ')
        x, y, z = positions.split(',')
        x = list(map(int, x[2:].split('..')))
        x[1] += 1
        x = range(*x)

        y = list(map(int, y[2:].split('..')))
        y[1] += 1
        y = range(*y)

        z = list(map(int, z[2:].split('..')))
        z[1] += 1
        z = range(*z)
        parsed.append((state, x, y, z))
    return parsed

def countOnLights(board):
    total = 0
    for plane in board:
        for line in plane:
            for c in line:
                if c == '#':
                    total += 1
    return total

def calculateOverlap(cube1, cube2):
    xOverlap = set(cube1[0]) & set(cube2[0])
    yOverlap = set(cube1[1]) & set(cube2[1])
    zOverlap = set(cube1[2]) & set(cube2[2])

    return len(xOverlap) * len(yOverlap) * len(zOverlap)

def calcOverlap(input):
    total = 0
    for i, cube1 in enumerate(input):
        for j, cube2 in enumerate(input[:i]):
            cube2size = 

def part1(input):
    return -1
    parsedInput = parseInput(input)
    parsedInput = [ line for line in parsedInput if max(line[1]) <= 50 and min(line[1]) >= -50 ]
    pp.pprint(parsedInput)
    board = buildEmptyBoard()
    for line in parsedInput:
        for pos in itertools.product(line[1], line[2], line[3]):
            board = setBoardPosition(board, pos, '.' if line[0] == 'off' else '#')
    return countOnLights(board)

def part2(input):
    return None
