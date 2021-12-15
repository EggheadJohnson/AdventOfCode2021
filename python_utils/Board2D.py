class Board2D:
    def __init__(self, positions):
        self.board = [ list(map(int, list(line))) for line in positions]
    def printBoard(self, separator=''):
        boardMaxVal = max([max(line) for line in self.board])
        boardMaxLen = len(str(boardMaxVal))
        for line in self.board:
            print(separator.join(map(str, line)))
    def getPosition(self, position):
        return self.board[position[0]][position[1]]
    def setPosition(self, position, value):
        self.board[position[0]][position[1]] = value
    def isPositionInBoard(self, position):
        return position[0] >= 0 and position[0] < len(self.board) and position[1] >= 0 and position[1] < len(self.board[0])
    def getAdjacentPositions(self, position):
        return list(filter(self.isPositionInBoard, [
            (position[0] - 1, position[1]),
            (position[0] + 1, position[1]),
            (position[0], position[1] - 1),
            (position[0], position[1] + 1),
        ]))
    def getLastPosition(self):
        return (len(self.board) - 1, len(self.board[len(self.board) - 1]) - 1)
