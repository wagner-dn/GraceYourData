#! /usr/bin/env python

### Written by Dominique Neitzel Wagner and Grace Bottom, December 2014

import sys
import re
import itertools

"""This script generates genepop files of all combinations (withouth replacement) 
of pairs of populations from an input genepopfile with many populations.

The input syntax is: inputfile pop1 pop2 ...popN"""

allpops = sys.argv[1]
poplist = sys.argv[2:]
combos = list(itertools.combinations(poplist,2))

for pair in combos:
	infile = open(allpops, 'r')
	popnames_str = "_".join(pair)
	outfilename = popnames_str+"_genepop.txt"
	outfile=open(outfilename, 'a')
	for line in infile:
		if line.startswith("Pop"):
			break
		outfile.write(line)
	infile.close()
	for pop in pair:
		infile = open(allpops, 'r')
		outfile.write('Pop\n')
		for line in infile:
			line=line.rstrip()
			if re.search(str(pop),line):
				outfile.write(line+"\n")
		infile.close()

outfile.close()
