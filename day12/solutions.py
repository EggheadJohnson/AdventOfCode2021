import pprint, collections

pp = pprint.PrettyPrinter(indent=4)

def buildMap(input):
    fullMap = collections.defaultdict(list)
    for line in input:
        line = line.split('-')
        if line[0].isupper() and line[1].isupper():
            print("PANIC!!!! ON LINE {}".format(line))

        fullMap[line[0]].append(line[1])
        fullMap[line[1]].append(line[0])
    return fullMap

def performBFS(fullMap, allPaths, seen):

    if not seen:
        pos = 'start'
    else:
        pos = seen[-1]
    for nextStep in fullMap[pos]:
        if nextStep == 'end':
            seen.append(nextStep)
            allPaths.append(''.join(seen))
            continue
        elif nextStep.islower() and nextStep in seen:
            continue
        allPaths = performBFS(fullMap, allPaths, seen + [nextStep])
    return allPaths


def performBFS_B(fullMap, allPaths, seen, haveDoubleVisitedSomewhere):

    if not seen:
        pos = 'start'
    else:
        pos = seen[-1]
    for nextStep in fullMap[pos]:
        if nextStep == 'start':
            continue
        if nextStep == 'end':
            seen.append(nextStep)
            allPaths.append(','.join(seen))
            continue
        elif nextStep.islower() and nextStep in seen:
            if haveDoubleVisitedSomewhere:
                continue
            allPaths = performBFS_B(fullMap, allPaths, seen + [nextStep], nextStep in seen)
            continue
        allPaths = performBFS_B(fullMap, allPaths, seen + [nextStep], haveDoubleVisitedSomewhere)
    return allPaths

def part1(input):
    fullMap = buildMap(input)
    allPaths = []
    seen = [ 'start' ]
    allPaths = performBFS(fullMap, allPaths, seen)
    return len(allPaths)

def part2(input):
    fullMap = buildMap(input)
    allPaths = []
    seen = [ 'start' ]
    allPaths = set(performBFS_B(fullMap, allPaths, seen, False))
    return len(allPaths)
