def fromBinaryString(binaryString, zeroChar='.', oneChar='#'):
    x = len(binaryString) - 1
    tot = 0
    valueDict = {
        zeroChar: 0,
        oneChar: 1
    }
    for i, c in enumerate(binaryString):
        tot += valueDict[c] * 2**x
        x -= 1
    return tot
