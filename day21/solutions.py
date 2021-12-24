import pprint, sys
from collections import deque
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

def part2TheDumbWay(input):
    maxPoints = 8
    # list of games, each game is a tuple of player tuples (pos, points)
    games = deque([
        (
            (8, 0), (4, 0)
        )
    ])
    finishedGames = []
    while games:
        game = games.popleft()
        if game[0][1] < maxPoints and game[1][1] < maxPoints:
            for i in range(3):
                p1newPos = ((game[0][0] + i - 1) % 10) + 1
                p1newPts = game[0][1] + game[0][0]
                if p1newPts > maxPoints:
                    finishedGames.append(((p1newPos, p1newPts), game[1]))
                else:
                    games.append(((p1newPos, p1newPts), game[1]))
            for i in range(3):
                p2newPos = ((game[1][0] + i - 1) % 10) + 1
                p2newPts = game[1][1] + game[1][0]
                if p2newPts > maxPoints:
                    finishedGames.append((game[0], (p2newPos, p2newPts)))
                else:
                    games.append((game[0], (p2newPos, p2newPts)))
    print(len(finishedGames))




def part2(input):
    part2TheDumbWay(input)
    return None
