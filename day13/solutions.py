import pprint

pp = pprint.PrettyPrinter(indent=4)

def getListOfPoints(input):
    return [tuple(map(int, line.split(','))) for line in input if ',' in line]

def getListOfFolds(input):
    return list(map(lambda fold: (fold[0], int(fold[1])), [line.split('fold along ')[1].split('=') for line in input if 'fold along' in line]))

def performHorizFold(points, fold):
    return [ (point[0], 2*fold[1] - point[1]) if point[1] > fold[1] else point for point in points  ]

def performVertFold(points, fold):
    return [ (2*fold[1] - point[0], point[1]) if point[0] > fold[1] else point for point in points ]

def performFolds(points, folds):
    for fold in folds:
        if fold[0] == 'y':
            points = list(set(performHorizFold(points, fold)))
        else:
            points = list(set(performVertFold(points, fold)))
    return points

def printPoints(points):
    max_x = 0
    max_y = 0
    board = []
    for i, j in points:
        if i > max_x:
            max_x = i
        if j > max_y:
            max_y = j
    for i in range(max_y + 1):
        line = []
        for j in range(max_x + 1):
            line.append('.')
        board.append(line)

    for point in points:
        board[point[1]][point[0]] = '#'

    print('~' * (max_x + 1))
    for line in board:
        print(''.join(line))
    print('~' * (max_x + 1))

def part1(input):
    points = getListOfPoints(input)
    folds = getListOfFolds(input)
    points = performFolds(points, folds[:1])
    return len(points)

def part2(input):
    points = getListOfPoints(input)
    folds = getListOfFolds(input)
    points = performFolds(points, folds)
    printPoints(points)
    return len(points)
