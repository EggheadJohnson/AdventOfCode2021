import pprint

pp = pprint.PrettyPrinter(indent=4)

def parseReactions(reactionsInput):
    reactions = {}
    for line in reactionsInput:
        key, val = line.split(' -> ')
        reactions[tuple(key)] = val
    return reactions

def takeOneStep(compound, reactions):
    return ''.join([ pair[0] + reactions[pair] for pair in zip(compound[:-1], compound[1:])] ) + compound[-1]

def getSplitCompound(compound):
    splitCompound = {}
    for pair in zip(compound[:-1], compound[1:]):
        splitCompound[pair] = splitCompound.get(pair, 0) + 1
    return splitCompound

def takeNewStep(splitCompound, reactions):
    inputCompoundPairs = splitCompound.keys()
    changes = {}
    for pair in inputCompoundPairs:
        result = reactions[pair]
        newPairs = (pair[0], result), (result, pair[1])
        changes[newPairs[0]] = changes.get(newPairs[0], 0) + splitCompound[pair]
        changes[newPairs[1]] = changes.get(newPairs[1], 0) + splitCompound[pair]
    return changes

def getCounts(compound):
    compoundCounts = {}
    for c in compound:
        compoundCounts[c] = compoundCounts.get(c, 0) + 1
    return compoundCounts

def getNewCounts(splitCompound):
    compoundCounts = {}
    for key, val in splitCompound.items():
        for c in key:
            compoundCounts[c] = compoundCounts.get(c, 0) + val/2
    return compoundCounts

def minMaxCompoundCounts(compoundCounts):
    min = None
    max = None
    for c in compoundCounts:
        if not min or compoundCounts[c] < compoundCounts[min]:
            min = c
        if not max or compoundCounts[c] > compoundCounts[max]:
            max = c
    return min, max


def part1(input):
    compound = input[0]
    reactions = input[2:]
    reactions = parseReactions(reactions)
    splitCompound = getSplitCompound(compound)
    for x in range(10):
        compound = takeOneStep(compound, reactions)
        splitCompound = takeNewStep(splitCompound, reactions)

    print('ISSUES FOUND')
    for pair in splitCompound:
        if splitCompound[pair] != getSplitCompound(compound)[pair]:
            print('diff', pair, splitCompound[pair], getSplitCompound(compound)[pair])
    for pair in getSplitCompound(compound):
        if splitCompound[pair] != getSplitCompound(compound)[pair]:
            print('ffid', pair, getSplitCompound(compound)[pair], splitCompound[pair])
    print('END ISSUES FOUND')

    compoundCounts = getCounts(compound)
    newCompoundCounts = getNewCounts(splitCompound)
    newCompoundCounts[input[0][0]] += 0.5
    newCompoundCounts[input[0][-1]] += 0.5
    min, max = minMaxCompoundCounts(compoundCounts)
    newMin, newMax = minMaxCompoundCounts(newCompoundCounts)
    return compoundCounts[max] - compoundCounts[min], newCompoundCounts[newMax] - newCompoundCounts[newMin]

def part2(input):
    compound = input[0]
    reactions = input[2:]
    reactions = parseReactions(reactions)
    splitCompound = getSplitCompound(compound)
    for x in range(40):
        splitCompound = takeNewStep(splitCompound, reactions)
    newCompoundCounts = getNewCounts(splitCompound)
    newCompoundCounts[input[0][0]] += 0.5
    newCompoundCounts[input[0][-1]] += 0.5
    newMin, newMax = minMaxCompoundCounts(newCompoundCounts)
    return newCompoundCounts[newMax] - newCompoundCounts[newMin]
