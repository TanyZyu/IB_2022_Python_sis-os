#!/usr/bin/python3

import argparse
import os.path

# Make a parser
parser = argparse.ArgumentParser(prog= 'rm',
                                 description = 'remove directories') # wc counts lines, words and bytes
parser.add_argument('-r', action='store_true') # define flag -a: if present, put TRUE in dictionary
args = parser.parse_args() # make dictionary 'dirs'(list of files)

# Define deleting function
def del_file(f):
    if not os.path.isdir(f): # check if the x is directory
        os.remove('f') # if no, delete f
    else:
        d_contains = os.listdir(path=f)  # if yes, "unpack" it
        if len(d_contains) == 0: # if directory is empty, delete it
            os.remove('f')
        elif not args.r:  # if not empty, Respect options
            print('rm: ', f, ': is a directory', sep='') # if no '-r', print warning
        else: # if '-r' is present, call function recursively
            for d in d_contains:
                del_file(d)

# Call deleting function to each position argument
for d in args.dirs:
    del_file(d)
