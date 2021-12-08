import pprint
from statistics import mean, median
from math import ceil

pp = pprint.PrettyPrinter(indent=4)

def part1(input):
    positions = [ int(i) for i in input[0].split(',') ]
    targetPos = median(positions)

    return int(sum([abs(i - targetPos) for i in positions]))

def part2(input):
    positions = [ int(i) for i in input[0].split(',') ]
    targetPos = ceil(mean(positions))
    return min([ sum(map(lambda p: sum(range(1, abs(i-p)+1)), positions)) for i in range(targetPos - 2, targetPos + 3)])
