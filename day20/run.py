import os
from solutions import part1, part2
import argparse

'''
➜  day20 git:(main) ✗ time python3 run.py --puzzle
Opening /puzzle.txt
result Part 1: 4964
result Part 2: 13202
python3 run.py --puzzle  28.88s user 0.02s system 99% cpu 28.906 total
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
