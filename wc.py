#!/usr/bin/python3

import sys
import argparse
import numpy as np
import re

# Make a parser
parser = argparse.ArgumentParser(prog= 'wc',
                                 description = 'count') # wc counts lines, words and bytes
parser.add_argument('-c', action='store_true') # define flag -c: byte counts (if present, put TRUE in dictionary)
parser.add_argument('-w', action='store_true') # define flag -w: the word counts (if present, put TRUE in dictionary)
parser.add_argument('-l', action='store_true') # define flag -l: newline counts (if present, put TRUE in dictionary)
parser.add_argument('dirs', nargs="*") # define position argument (files), their count (*)
args = parser.parse_args() # make dictionary of four: 'c', 'w', 'l' (True/False) and 'dirs'(list of files)

# Collect data for all files to the same array
table = np.empty((0, 4)) # create an empty np array containing 4 columns
for f in args.dirs: # for each "position argument" ...
    size = sys.getsizeof(f) # calculate size
    with open(f) as fl:
      text = fl.read() # first, read file into variable (to avoid reading file after EOF)
      words = len(text.split()) # calculate words count
      lines = text.count('\n') # calculate words count
    newrow = (lines, words, size, f) #create a row containing info on each file
    table = np.vstack([table, newrow]) # append row to the array

# Respect options, print result
if (args.l and args.w and args.c) or (not args.l and not args.w and not args.c):
  print(re.sub('( \[|\[|\'|\])', '', str(table[:,0:4])))
elif args.l:
  if args.c and (not args.w):
    print(re.sub('( \[|\[|\'|\])', '', str(table[:,[0, 2, 3]])))
  elif args.w and (not args.c):
    print(re.sub('( \[|\[|\'|\])', '', str(table[:,[0, 1, 3]])))
  else:
    print(re.sub('( \[|\[|\'|\])', '', str(table[:, [0, 3]])))

elif args.c:
  if args.w:
    print(re.sub('( \[|\[|\'|\])', '', str(table[:,[1, 2, 3]])))
  else:
    print(re.sub('( \[|\[|\'|\])', '', str(table[:,[2, 3]])))

elif args.w:
  print(re.sub('( \[|\[|\'|\])', '', str(table[:,[1, 3]])))
