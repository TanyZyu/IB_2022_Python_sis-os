#!/usr/bin/python3

import argparse
import os.path

# Make a parser
parser = argparse.ArgumentParser(prog= 'ls',
                                 description = 'Show files in directory') # Add description of programm
parser.add_argument('-a', action='store_true') # define flag -a: if present, put TRUE in dictionary
parser.add_argument('dirs', nargs="*", default=".") # define position argument (directories), their count (*)
args = parser.parse_args() # make dictionary of two: '-a'(True/False) and 'dirs'(list of directories)

# Collect name of all files and folders to the same list
files = list()
for d in args.dirs: # for each "position argument" ...
    if not os.path.isdir(d): # ... check if it is directory
        files.append(d) # if not, put it directly to the list of files
    elif os.path.exists(d): # else check if the path is correct
        d_cont = os.listdir(path=d) # if yes, "unpack" it
        files.extend(d_cont) # append to the list of files

# Respect options
if not args.a: # if no -a flag is present "don't show hidden files"
    files = [x for x in files if not x.startswith('.')] # keep only elements not starting with dot

# Show result
files.sort()
print(*files, sep='\t')
