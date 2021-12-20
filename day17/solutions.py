import pprint, sys, functools
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

def getTarget(line):
    # target area: x=20..30, y=-10..-5
    line = line.split(': ')[1]
    x, y = line.split(', ')
    x = tuple(map(int, x[2:].split('..')))
    y = tuple(map(int, y[2:].split('..')))
    return x, y

def getTriangleNumbers(i=100):
    triangleNums = [1]
    for j in range(2, i+1):
        triangleNums.append(triangleNums[-1] + j)
    return triangleNums

def getPositionsDownTo(iv, yTarget):
    pv = 0
    while pv > min(yTarget):
        pv += iv
        iv -= 1
        # print(pv, iv)
        if pv <= max(yTarget) and pv >= min(yTarget):
            return True
    return False

def part1(input):

    xTarget, yTarget = getTarget(input[0])
    print(getPositionsDownTo(77, yTarget))
    compMethod = sorted(filter(lambda x: x[1], [(i, getPositionsDownTo(i, yTarget)) for i in range(1, 80)]), reverse=True)
    pp.pprint(compMethod[:5])
    pp.pprint((xTarget, yTarget))
    triangleNums = getTriangleNumbers(80)
    for i in range(len(triangleNums) - 1, -1, -1):
        for j in range(len(triangleNums) - 1, -1, -1):
            if triangleNums[i] - triangleNums[j] in range(yTarget[0], yTarget[1]+1):
                print(i, j, triangleNums[i], triangleNums[j])
                return j
    return None

def getAllFuturePositionsForVelocity(velocity, target):
    position = (0, 0)
    while position[0] <= max(target[0]) and position[1] >= min(target[1]):
        position = (position[0] + velocity[0], position[1] + velocity[1])
        if velocity[0] != 0:
            velocity[0] += -1 * (velocity[0] / abs(velocity[0]))
        velocity[1] -= 1
        print('pos: {} vel: {}'.format(position, velocity))

def getYSteps(yVelocities, yTarget):
    stepCtr = {}
    for vy0 in yVelocities:
        ypos = 0
        steps = 0
        vy = vy0
        while ypos not in range(yTarget[0], yTarget[1]+1):
            ypos += vy
            vy -= 1
            steps += 1
        if steps not in stepCtr:
            stepCtr[steps] = set()
        stepCtr[steps].add(vy0)
    return stepCtr

def getXSteps(xVelocity, xTarget):
    stepCtr = 0
    xPos = 0
    steps = []
    while xVelocity > 0 and xPos <= max(xTarget):
        xPos += xVelocity
        xVelocity -= 1
        stepCtr += 1
        if xPos in range(xTarget[0], xTarget[1] + 1):
            steps.append(stepCtr)
    return steps

def getPotentialXVelocities(xTarget):
    xMax = max(xTarget)
    xMin = min(xTarget)
    potentialVelocities = getTriangleNumbers(xMax)
    xVelocitiesBySteps = {}
    for xv in range(xMax):
        steps = getXSteps(xv, xTarget)
        for step in steps:
            if step not in xVelocitiesBySteps:
                xVelocitiesBySteps[step] = set()
            xVelocitiesBySteps[step].add(xv)
    return xVelocitiesBySteps


def part2(input):
    xTarget, yTarget = getTarget(input[0])
    compMethod = sorted(filter(lambda x: x[1], [(i, getPositionsDownTo(i, yTarget)) for i in range(-80, 80)]), reverse=True)
    yVelocities = list(map(lambda x: x[0], compMethod))
    yStepCtr = getYSteps(yVelocities, yTarget)
    xStepCtr = getPotentialXVelocities(xTarget)
    pp.pprint(len(compMethod))
    pp.pprint(yVelocities)
    pp.pprint(yStepCtr)
    pp.pprint(xStepCtr)

    velocities = []
    for keyVY in yStepCtr:
        print('key: ', keyVY)
        pp.pprint(yStepCtr[keyVY])
        pp.pprint(xStepCtr.get(keyVY, []))
        velocities.append(len(yStepCtr[keyVY]) * len(xStepCtr.get(keyVY, [])))

    return sum(velocities)
