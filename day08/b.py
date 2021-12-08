from a import splitInput
from functools import reduce

def hasOne(line):
    return len([ d for d in line if len(d) == 2 ]) > 0

def hasSeven(line):
    return len([ d for d in line if len(d) == 3 ]) > 0

def findZero(line):
    middle = findMiddle(line)
    eight = findEight(line)
    return ''.join(sorted( [ digit for digit in line if set(digit) == (set(eight) - set([middle]))][0]))

def findOne(line):
    return ''.join(sorted([ digit for digit in line if len(digit) == 2][0]))

def findTwo(line):
    six = set(findSix(line))
    nine = set(findNine(line))
    corners = six ^ nine
    return ''.join(sorted(corners | set(findTop(line)) | set(findMiddle(line)) | set(findBottom(line))))

def findThree(line):
    return ''.join(sorted([digit for digit in line if len(digit) == 5 and ''.join(sorted(digit)) not in set([findTwo(line), findFive(line)])][0]))

def findFour(line):
    return ''.join(sorted([ digit for digit in line if len(digit) == 4][0]))

def findFive(line):
    zero = findZero(line)
    sixes = set()
    for digit in line:
        if len(digit) == 6:
            sixes.add(tuple(sorted(digit)))
    sixes.remove(tuple(zero))
    i = iter(sixes)
    five = set(next(i))
    return ''.join(sorted(five & set(next(i))))

def findSix(line):
    return ''.join(sorted([digit for digit in line if len(digit) == 6 and ''.join(sorted(digit)) not in set([findZero(line), findNine(line)])][0]))

def findSeven(line):
    return ''.join(sorted([ digit for digit in line if len(digit) == 3][0]))

def findEight(line):
    return ''.join(sorted([ digit for digit in line if len(digit) == 7][0]))

def findNine(line):
    return ''.join(sorted(set(findFour(line)) | set(findTop(line)) | set(findBottom(line))))

def findTop(line):
    one = set(findOne(line))
    seven = set(findSeven(line))
    return next(iter(seven - one))

def findMiddle(line):
    top = findTop(line)
    four = set([ digit for digit in line if len(digit) == 4][0])
    fives = set()
    for digit in line:
        if len(digit) == 5:
            fives.add(tuple(sorted(digit)))
    i = iter(fives)
    centers = set(next(i))
    centers = centers & set(next(i))
    centers = centers & set(next(i))
    return next(iter(centers & four))

def findBottom(line):
    five = set(findFive(line))
    top = set(findTop(line))
    four = set(findFour(line))
    return next(iter(five - four - top))

def buildValueMap(line):
    return {
        findZero(line): '0',
        findOne(line): '1',
        findTwo(line): '2',
        findThree(line): '3',
        findFour(line): '4',
        findFive(line): '5',
        findSix(line): '6',
        findSeven(line): '7',
        findEight(line): '8',
        findNine(line): '9',
    }

def findOutputVal(valueMap, output):
    outputNumber = ''.join([valueMap[''.join(sorted(o))] for o in output])
    return int(outputNumber)

def b(input, pp):
    signals, outputs = splitInput(input)
    total = 0
    for i, signal in enumerate(signals):
        line = signal + outputs[i]
        valueMap = buildValueMap(line)
        total += findOutputVal(valueMap, outputs[i])
    return total
