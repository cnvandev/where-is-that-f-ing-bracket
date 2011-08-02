import sys
import os
from collections import Counter
from termcolor import colored

VERBOSE = False
IGNORE_TEST = True

def count_compare(count, symbol1, symbol2):
    ''' Prints a warning if you have more of one symbol than another '''
    if count[symbol2] - count[symbol1] != 0 or VERBOSE:
        print colored(symbol1 + ' = ' + str(count[symbol1]) +
                      ' and ' + symbol2 + ' = ' + str(count[symbol2]) +
                      ' ... delta = ' + str(count[symbol2] - count[symbol1]),
                      'red')

def count(path):
    ''' Runs the count_brackets function on all files in a directory, regardless of depth '''
    dirs = []
    files = []
    
    for thing in os.listdir(path):
        if os.path.isfile(os.path.join(path, thing)) and thing[-2:] == 'js':
            files.append(thing)
        elif os.path.isdir(os.path.join(path, thing)) and (thing not in ('t', 'test') and IGNORE_TEST):
            dirs.append(thing)

    for filename in files:
        print "-", os.path.join(path, filename)
        count_brackets(os.path.join(path, filename))

    for directory in dirs:
        count(os.path.join(path, directory))

def count_brackets(filename):
    ''' Counts bracket types in a file '''
    count = Counter(open(filename, 'r').read())
    count_compare(count, '[', ']')
    count_compare(count, '(', ')')
    count_compare(count, '{', '}')

count(sys.argv[1])
