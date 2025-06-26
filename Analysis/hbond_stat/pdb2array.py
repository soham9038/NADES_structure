import math
import os

def pdb2array(pdb):
    lines, index = file_len(pdb)
    #name=str(os.path.splitext("pdb")[0])
    n = 0
    s = -1
    list1 = []
    list3 = {}
    fname=pdb
#    lines=name+'line'
    while n < lines:
        s = s + 1
        list2 = []
        with open(fname) as pdbfile:
            for i, line in enumerate(pdbfile):
                if n<=i<=n+index-1:
                    list1 = line.split()
                    #print(list1)
                    list2.append(list1[5:8])
                    list3[s] = list2

        n=n+index
#        name+'list' = list3

    return list3
