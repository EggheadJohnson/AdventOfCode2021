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

# you have to guarantee the line starts with a packet.
def extractPackets(line):
    allPackets = []
    version = line[:3]
    type = line[3:6]
    packet = version + type # yes i know i just separated them leave me alone
    print(version, type, packet, line)
    if type == '100':
        i = 6
        digits = 'a' # obvs wrong initial value
        while digits[0] != '0':
            digits = line[i:i+5]
            packet += digits
            i += 5
        allPackets.append(packet)
    else:
        I = line[6]
        packet += I
        if I == '0':
            # based on total subpacket length
            packetLength = binaryStringToDecimal(line[7:22])
            subPackets = []
            while sum(map(len, subPackets)) < packetLength:
                subPackets.extend(extractPackets(line[22+sum(map(len, subPackets)):22+packetLength]))
            allPackets.append(line[:22+packetLength])
            allPackets.extend(subPackets)
        if I == '1':
            # based on count of subpackets
            packetCount = binaryStringToDecimal(line[7:18])
            subPackets = []
            while len(subPackets) < packetCount:
                subPackets.extend(extractPackets(line[18+sum(map(len, subPackets)):]))
            allPackets.append(line[:18+sum(map(len, subPackets))])
            allPackets.extend(subPackets)
    return allPackets

def part1(input):
    packets = extractPackets(hexToBin(input[0]))
    pp.pprint(packets)
    return sum([binaryStringToDecimal(line[:3]) for line in packets])

def part2(input):
    return None
