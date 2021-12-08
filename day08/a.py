def splitInput(input):
    signals = []
    outputs = []
    for line in input:
        signal, output = line.split(' | ')
        signals.append(signal.split(' '))
        outputs.append(output.split(' '))
    return signals, outputs

def a(input, pp):
    signals, outputs = splitInput(input)
    total = 0
    for output in outputs:
        total += len([ o for o in output if len(o) in (2, 3, 4, 7) ])
    return total
