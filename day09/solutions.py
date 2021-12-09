import pprint, itertools
from functools import reduce

pp = pprint.PrettyPrinter(indent=4)
def mapInput(input):
    print('height: {} width: {}'.format(len(input), len(input[0])))
    return list(map(lambda line: list(map(lambda i: int(i), list(line))), input))

def getListOfSpots(height, width):
    return set(itertools.product(range(height), range(width)))

def part1(input):
    low_points = []
    array_input = mapInput(input)
    for i, line in enumerate(array_input):
        for j, spot in enumerate(line):
            debug_line = '{} - {}'.format((i, j), spot)
            if i > 0 and spot >= array_input[i-1][j]:
                continue
            if i < len(array_input) - 1 and spot >= array_input[i+1][j]:
                continue
            if j > 0 and spot >= array_input[i][j-1]:
                continue
            if j < len(array_input[i]) - 1 and spot >= array_input[i][j+1]:
                continue
            low_points.append((i, j))

    return sum(map(lambda p: array_input[p[0]][p[1]] + 1, low_points))

def getAdjacent(pos):
    return [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]

def filterAdjacent(adjacent, input, seen):
    return list(filter(lambda x: x not in seen and x[0] >= 0 and x[0] < len(input) and x[1] >= 0 and x[1] < len(input[0]), adjacent))

def getBasin(pos, input, seen):
    basin = set()
    queue = filterAdjacent(getAdjacent(pos), input, seen)
    while queue:
        spot = queue.pop()
        seen.add(spot)
        if input[spot[0]][spot[1]] != '9':
            basin.add(spot)
            queue.extend(filterAdjacent(getAdjacent(spot), input, seen))
    return tuple(basin)

def part2(input):
    seen = set()
    basins = []

    for i in range(len(input)):
        for j in range(len(input[i])):
            pos = (i, j)
            if pos not in seen and input[i][j] != '9':
                basin = getBasin(pos, input, seen)
                basins.append(basin)
    basins = sorted(basins, key=len, reverse=True)

    return reduce(lambda carry, val: carry*len(val), basins[:3], 1)
