import pprint, sys
sys.path.append('../python_utils')

from Board2D import Board2D
from dijkstra import dijkstra

pp = pprint.PrettyPrinter(indent=4)

def binaryStringToDecimal(binStr):
    i = len(binStr) - 1
    tot = 0
    for j, c in enumerate(binStr):
        tot += int(c) * 2**i
        i -= 1
    return tot

def hexToBin(line):
    hexToBinDict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    return ''.join([hexToBinDict[c] for c in line])

def part1(input):
    return None

def part2(input):
    return None
