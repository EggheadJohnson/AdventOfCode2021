import os
from solutions import part1, part2
import argparse

'''
➜  day15 git:(main) ✗ time python3 run.py --puzzle
Opening /puzzle.txt
result Part 1: 673
result Part 2: 2893
python3 run.py --puzzle  20.44s user 0.05s system 99% cpu 20.500 total
'''

parser = argparse.ArgumentParser()
parser.add_argument('--puzzle', action='store_true', help='Use the live puzzle data')
args = parser.parse_args()

file_path = os.path.dirname(os.path.realpath(__file__))
file_name = '/sample.txt'
if args.puzzle:
    file_name = '/puzzle.txt'
input_path = file_path + file_name

print('Opening {}'.format(file_name))

inpt = [ line.strip() for line in open(input_path, 'r')]

print("result Part 1:", part1(inpt))
print("result Part 2:", part2(inpt))
