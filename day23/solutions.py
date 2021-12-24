import pprint, sys, copy, os
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HIGHLIGHT = '\033[47m'

def scanBoard(input):
    board = []
    pieces = {}
    for i, inLine in enumerate(input):
        outLine = []
        if len(inLine) < len(input[0]):
            inLine = '..' + inLine + '..'
        for j, c in enumerate(inLine):
            if c == '#':
                outLine.append('#')
            else:
                outLine.append('.')
            if c in 'ABCD':
                if c in pieces:
                    c = c.lower()
                pieces[c] = (i, j)

        board.append(outLine)
    return board, pieces

def getColor(piece, highlight, loc):
    hl = ''
    if highlight:
        hl = bcolors.HIGHLIGHT
    if piece in 'Aa':
        if loc[1] == 3 and loc[0] in range(2, 4):
            return hl + bcolors.OKGREEN
        return hl + bcolors.FAIL
    if piece in 'Bb':
        if loc[1] == 5 and loc[0] in range(2, 4):
            return hl + bcolors.OKGREEN
        return hl + bcolors.FAIL
    if piece in 'Cc':
        if loc[1] == 7 and loc[0] in range(2, 4):
            return hl + bcolors.OKGREEN
        return hl + bcolors.FAIL
    if piece in 'Dd':
        if loc[1] == 9 and loc[0] in range(2, 4):
            return hl + bcolors.OKGREEN
        return hl + bcolors.FAIL

def printBoard(board, pieces, highlight='', clear=True):
    outBoard = copy.deepcopy(board)
    rows, columns = map(int, os.popen('stty size', 'r').read().split())
    if clear:
        os.system('clear')

        for x in range(rows // 5):
            print()
    for piece, loc in pieces.items():
        # print(piece, loc)
        outBoard[loc[0]][loc[1]] = getColor(piece, piece == highlight, loc) + piece + bcolors.ENDC
    for line in outBoard:
        print(' ' * (columns//2 - len(board[0])//2) + ''.join(line))

def movePiece(board, pieces, piece, dir):
    pos = pieces[piece]
    newPos = (pos[0], pos[1])
    if dir in ('k', 'K'):
        newPos = (pos[0] - 1, pos[1])
    if dir in ('h', 'H'):
        newPos = (pos[0], pos[1] - 1)
    if dir in ('j', 'J'):
        newPos = (pos[0] + 1, pos[1])
    if dir in ('l', 'L'):
        newPos = (pos[0], pos[1] + 1)
    for p, v in pieces.items():
        if newPos == v:
            return board, pieces
    print(pos, newPos)
    if board[newPos[0]][newPos[1]] == '#':
        return board, pieces
    pieces[piece] = newPos
    return board, pieces


def runInteractive(board, pieces, rawInput):
    selection = ''
    pieceSelected = ''
    totalCost = 0
    while selection not in ('q', 'Q'):
        printBoard(board, pieces, pieceSelected)
        priorSelection = selection
        print('    Total cost: {}'.format(totalCost))
        print(' AaBbCcDd to select the piece you want to move')
        print(' h('+u"\u2190"+') j('+u"\u2193"+') k('+u"\u2191"+') l('+u"\u2192"+') to move')
        print(' q to quit, r to reset')
        selection = input('What you want: ')
        if selection in ('q', 'Q') and pieceSelected != '':
            pieceSelected = ''
        if selection in ('a', 'A', 'b', 'B', 'c', 'C', 'd', 'D'):
            pieceSelected = selection
        if selection in ('h', 'j', 'k', 'l', 'H', 'J', 'K', 'L') and priorSelection != '':
            posBeforeMove = pieces[pieceSelected]
            board, pieces = movePiece(board, pieces, pieceSelected, selection)
            if posBeforeMove != pieces[pieceSelected]:
                if pieceSelected in ('A', 'a'):
                    totalCost += 1
                if pieceSelected in ('B', 'b'):
                    totalCost += 10
                if pieceSelected in ('C', 'c'):
                    totalCost += 100
                if pieceSelected in ('D', 'd'):
                    totalCost += 1000
        if selection in ('r', 'R'):
            board, pieces = scanBoard(rawInput)
            selection = ''
            pieceSelected = ''
            totalCost = 0



def part1(input):
    board, pieces = scanBoard(input)
    runInteractive(board, pieces, input)
    return None

def part2(input):
    return None
