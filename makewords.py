#!/usr/bin/python
# Usage : ./makewords.py  | sort | uniq
import itertools

a=["A", "B","C"]
b=["0", "1", "2"]
c=["a", "b", "c"]


def printCombos(a,b,c):
	for r in itertools.product(a,b,c):
	    #print r[0]+r[1]+r[2]
	    #print r[0]+r[1]
	    #print r[0]+r[2]
	    for i in xrange(1, len(r)+1):
		for x in itertools.combinations(r, i):
		    print ''.join(x)

printCombos(a,b,c)

