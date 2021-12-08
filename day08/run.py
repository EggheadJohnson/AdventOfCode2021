import os
from a import a
from b import b
import pprint, argparse

'''
Opening /puzzle.txt
result A: 321
result B: 1028926
'''

parser = argparse.ArgumentParser()
parser.add_argument('--puzzle', action='store_true', help='Use the live puzzle data')
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

file_path = os.path.dirname(os.path.realpath(__file__))
file_name = '/sample.txt'
if args.puzzle:
    file_name = '/puzzle.txt'
input_path = file_path + file_name

print('Opening {}'.format(file_name))

inpt = [ line.strip() for line in open(input_path, 'r')]

print("result A:", a(inpt, pp))
print("result B:", b(inpt, pp))
