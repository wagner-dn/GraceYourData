#! /usr/bin/env python


### This is a python script to randomize samples into a designated number of groups containing a designated number of samples
### Written by Grace Bottum, October 2015
### Modified by Dominique Neitzel Wagner, January 2016


import random

## Create as many documents that you need groups, here we use 4
Aout = open("Atest.txt", 'w')
Bout = open("Btest.txt", 'w')
#Cout = open("Ctest.txt", 'w')
#Dout = open("Dtest.txt", 'w')

## indlist reads in a txt file containing a list of all samples in your VCF. There should be one sample on each line followed by a return
indlist = open("TagGBS_Pond2TvsU_list.txt", 'r')
LineNumber = 0
for Line in indlist:
	Line=Line.split('\t')
	random.shuffle(Line)
	
	#### Here assign how many samples in each group. Remember python begins counting on zero and does not include the final number i.e. here group A contains 19 indivduals
	
	A=Line[0:31]
	B=Line[31:43]
	#C=Line[29:35]
	#D=Line[35:]
	
	#### Here correct each string to reflect your chosen number assigned to each group
	Astring = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % \
	(A[0], A[1], A[2], A[3], A[4], A[5], A[6], A[7], A[8], A[9], A[10], A[11], A[12], A[13], A[14], A[15], A[16], A[17], A[18], A[19], A[20], A[21], A[22], A[23], A[24], A[25], A[26], A[27], A[28], A[29], A[30])
	Bstring = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s" % \
	(B[0], B[1], B[2], B[3], B[4], B[5], B[6], B[7], B[8], B[9], B[10], B[11])
	#Cstring = "%s\n%s\n%s\n%s\n%s\n%s" % \
	#(C[0], C[1], C[2], C[3], C[4], C[5])
	#Dstring = "%s\n%s\n%s\n%s\n%s\n%s\n%s" % \
	#(D[0], D[1], D[2], D[3], D[4], D[5], D[6])

### Write to files and close

Aout.write(Astring+"\n")
Bout.write(Bstring+"\n")
#Cout.write(Cstring+"\n")
#Dout.write(Dstring+"\n")
Aout.close()
Bout.close()
#Cout.close()
#Dout.close()
indlist.close()
