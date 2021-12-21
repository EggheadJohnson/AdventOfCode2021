import pprint, sys
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

def part1(input):
    playerPositions = [1, 10]
    playerPoints = [0, 0]
    rolls = 0
    die = 1
    playerCtr = 0
    while max(playerPoints) < 1000:
        playerPositions[playerCtr] += (3*die + 3)
        die += 3
        if die > 100:
            die -= 100
        playerPositions[playerCtr] = ((playerPositions[playerCtr] - 1) % 10) + 1
        playerPoints[playerCtr] += playerPositions[playerCtr]
        rolls += 3
        playerCtr += 1
        playerCtr %= 2
    return min(playerPoints) * rolls

def part2(input):
    return None
