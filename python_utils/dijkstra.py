
def getShortestCurrentPath(shortestPathDict, seenButNotVisited):
    min = None
    for k in seenButNotVisited:
        if not min or shortestPathDict[k] < shortestPathDict[min]:
            min = k
    return min


def dijkstra(board, startingPosition, endingPosition):
    shortestPathDict = {
        startingPosition: 0
    }
    visited = set()
    seenButNotVisited = set([(0, 0)])

    shortestPathPos = startingPosition

    while True:
        pos = getShortestCurrentPath(shortestPathDict, seenButNotVisited)
        if pos == endingPosition:
            return shortestPathDict[pos]
        for p in board.getAdjacentPositions(pos):
            if p not in visited:
                seenButNotVisited.add(p)
            if p not in shortestPathDict or board.getPosition(p) + shortestPathDict[pos] < shortestPathDict[p]:
                shortestPathDict[p] = board.getPosition(p) + shortestPathDict[pos]
            if p not in visited and shortestPathDict[p] < shortestPathDict[shortestPathPos]:
                shortestPathPos = p
        seenButNotVisited.remove(pos)
        visited.add(pos)
