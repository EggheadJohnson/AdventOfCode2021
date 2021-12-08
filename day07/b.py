from statistics import mean, median
from math import ceil

def b(input, pp):

    positions = [ int(i) for i in input[0].split(',') ]
    targetPos = ceil(mean(positions))
    return min([ sum(map(lambda p: sum(range(1, abs(i-p)+1)), positions)) for i in range(targetPos - 2, targetPos + 3)])
