from statistics import mean, median
def a(input, pp):
    positions = [ int(i) for i in input[0].split(',') ]
    targetPos = median(positions)

    return int(sum([abs(i - targetPos) for i in positions]))
