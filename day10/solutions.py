import pprint

pp = pprint.PrettyPrinter(indent=4)

def parseLine(line):
    closingBrackets = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    characterStack = []
    for c in line:
        if c in closingBrackets.values():
            characterStack.append(c)
        elif c in closingBrackets:
            if characterStack[-1] == closingBrackets[c]:
                characterStack.pop()
            else:
                return 'corrupt', c, characterStack
    if len(characterStack) > 0:
        return 'incomplete', '', characterStack
    return 'complete', '', []

def completeLine(line):
    openingBrackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    mappedLine = list(map(lambda c: openingBrackets[c], line))
    mappedLine.reverse()
    return mappedLine

def scoreLineCompletion(lineCompletion):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    total = 0
    for char in lineCompletion:
        total *= 5
        total += points[char]
    return total

def getCorruptCharPoints(corruptChar):
    return {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }[corruptChar]

def part1(input):
    return sum(map(lambda corrupt: getCorruptCharPoints(parseLine(corrupt)[1]), filter(lambda line: parseLine(line)[0] == 'corrupt', input)))

def part2(input):
    scores = sorted(map(lambda incomplete: scoreLineCompletion(completeLine(parseLine(incomplete)[2])), filter(lambda line: parseLine(line)[0] == 'incomplete', input)))
    return scores[len(scores)//2]
