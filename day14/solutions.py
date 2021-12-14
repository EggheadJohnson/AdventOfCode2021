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


def getCounts(compound):
    compoundCounts = {}
    for c in compound:
        compoundCounts[c] = compoundCounts.get(c, 0) + 1
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
    pp.pprint(compound)
    reactions = parseReactions(reactions)
    pp.pprint(reactions)
    min = None
    max = None
    prevMin = None
    prevMax = None
    for x in range(20):
        # if min and max:
        #     prevMin, prevMax = compoundCounts[min], compoundCounts[max]
        compound = takeOneStep(compound, reactions)
        # compoundCounts = getCounts(compound)
        #
        #
        # min, max = minMaxCompoundCounts(compoundCounts)
        # # print(compound)
        # print('max: {} {} min: {} {}'.format(max, compoundCounts[max], min, compoundCounts[min]))
        # if prevMax:
        #     print('max: {} val: {} delta: {} ratio: {}'.format(max, compoundCounts[max], compoundCounts[max] - prevMax, compoundCounts[max] / prevMax))
        # if prevMin:
        #     print('min: {} val: {} delta: {} ratio: {}'.format(min, compoundCounts[min], compoundCounts[min] - prevMin, compoundCounts[min] / prevMin))
        # print('max: {} {}% min: {} {}%'.format(max, compoundCounts[max]/len(compound), min, compoundCounts[min]/len(compound)))
    compoundCounts = getCounts(compound)
    # print(reactions)
    pp.pprint(compoundCounts)
    min, max = minMaxCompoundCounts(compoundCounts)
    print(min, max)
    return compoundCounts[max] - compoundCounts[min]

def part2(input):
    return -1
    compound = input[0]
    reactions = input[2:]
    pp.pprint(compound)
    reactions = parseReactions(reactions)
    for x in range(40):
        print(x, len(compound))
        compound = takeOneStep(compound, reactions)
    compoundCounts = getCounts(compound)
    # print(reactions)
    pp.pprint(compoundCounts)
    min, max = minMaxCompoundCounts(compoundCounts)
    print(min, max)
    return compoundCounts[max] - compoundCounts[min]
