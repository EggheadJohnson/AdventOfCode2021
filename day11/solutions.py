import pprint

pp = pprint.PrettyPrinter(indent=4)

def mapInput(input):
    return list(map(lambda line: list(map(int, line)), input))

def bumpEverySpot(mappedInput):
    return [ [i+1 for i in line] for line in mappedInput]

def getNeighborSpots(spot):
    i, j = spot
    return [
        (i-1, j-1),
        (i-1, j),
        (i-1, j+1),
        (i, j-1),
        (i, j+1),
        (i+1, j-1),
        (i+1, j),
        (i+1, j+1),
    ]

def filterNeighborsToBeOnBoard(board, neighbors):
    return list(filter(lambda spot: spot[0] >= 0 and spot[0] < len(board) and spot[1] >= 0 and spot[1] < len(board[0]), neighbors))

def executeOverflows(mappedInput):
    needToOverflow = []
    hasOverflowed = set()
    for i, line in enumerate(mappedInput):
        for j, octopus in enumerate(line):
            if octopus > 9 and (i, j) not in hasOverflowed:
                needToOverflow.append((i, j))
    while needToOverflow:
        spot = needToOverflow.pop()
        neighbors = filterNeighborsToBeOnBoard(mappedInput, getNeighborSpots(spot))
        hasOverflowed.add(spot)
        for neighbor in neighbors:
            i, j = neighbor
            mappedInput[i][j] += 1
            if mappedInput[i][j] > 9 and (i, j) not in hasOverflowed and (i, j) not in needToOverflow:
                needToOverflow.append((i, j))
    return mappedInput, len(hasOverflowed)

def resetOverflows(mappedInput):
    return [[i if i <= 9 else 0 for i in line] for line in mappedInput]

def takeSingleStep(mappedInput):
    shouldPrint = False
    if shouldPrint:
        pp.pprint(mappedInput)
    mappedInput = bumpEverySpot(mappedInput)
    if shouldPrint:
        pp.pprint(mappedInput)
    mappedInput, overflowCount = executeOverflows(mappedInput)
    if shouldPrint:
        pp.pprint(mappedInput)
    mappedInput = resetOverflows(mappedInput)
    if shouldPrint:
        pp.pprint(mappedInput)
    return mappedInput, overflowCount


def part1(input):
    shouldPrint = False
    totalOverflows = 0
    mappedInput = mapInput(input)
    for i in range(100):
        mappedInput, currentOverflows = takeSingleStep(mappedInput)
        totalOverflows += currentOverflows
        if shouldPrint:
            pp.pprint(mappedInput)
    return totalOverflows

def part2(input):
    shouldPrint = False
    currentOverflows = 0
    mappedInput = mapInput(input)
    i = 0
    while currentOverflows < (len(input) * len(input[0])):
        mappedInput, currentOverflows = takeSingleStep(mappedInput)
        if shouldPrint:
            pp.pprint(mappedInput)
        i += 1
    return i
