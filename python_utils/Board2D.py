from collections import deque

class Board2D:
    def __init__(self, positions):
        self.board = deque([deque(line) for line in positions])
    def printBoard(self, separator=''):
        for line in self.board:
            print(separator.join(map(str, line)))
    def printIntBoard(self, separator=''):
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
    def getNineSpotsCenteredAtPos(self, position):
        return list(filter(self.isPositionInBoard, [
            (position[0] - 1, position[1] - 1),
            (position[0] - 1, position[1]),
            (position[0] - 1, position[1] + 1),

            (position[0], position[1] - 1),
            (position[0], position[1]),
            (position[0], position[1] + 1),

            (position[0] + 1, position[1] - 1),
            (position[0] + 1, position[1]),
            (position[0] + 1, position[1] + 1),

        ]))
    def getLastPosition(self):
        return (len(self.board) - 1, len(self.board[len(self.board) - 1]) - 1)
    def convertBoardToInts(self):
        self.board = deque([ deque(map(int, list(line))) for line in self.board])
    def padBoard(self, padVal='.'):
        for l in self.board:
            l.appendleft(padVal)
            l.append(padVal)
        top = []
        bot = []
        for i in range(len(self.board[0])):
            top.append(padVal)
            bot.append(padVal)
        self.board.appendleft(deque(top))
        self.board.append(deque(bot))
