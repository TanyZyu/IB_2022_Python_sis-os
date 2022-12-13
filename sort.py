#!/usr/bin/python3

import argparse

# Make a parser
parser = argparse.ArgumentParser(prog= 'sort',
                                 description = 'sort') # wc counts lines, words and bytes
args = parser.parse_args() # make dictionary 'dirs'(list of files)
for f in args.dirs: # for each file in "position argument" ...
    with open(f) as fl:
      text = fl.readlines() # read lines of file into string variable
      sortedtxt = sorted(text, key=str.casefold) # sort lines in case-insensitive mode
      print(*sortedtxt, sep= '\n')
