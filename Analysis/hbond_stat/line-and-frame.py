import math
import os
def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        line1 = i + 1
        n=0
        list1= {}
        with open(fname) as pdbfile:
                         for i, line in enumerate(pdbfile):
                               if n<=i<=line1:
                                    list1 = line.split()
                               if i==0:
                                    first=list1[1]
                               elif list1[1] == first:
                                    frame = i
                                    break

        n=n+1
        return line1, i
