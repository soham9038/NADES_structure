import math
import os
exec(open("line-and-frame.py").read())
exec(open("pdb2array.py").read())
exec(open("define-donor.py").read())
OWlist = pdb2array("OW.pdb")
HW1list = pdb2array("HW1.pdb")
HW2list = pdb2array("HW2.pdb")
O0Alist = pdb2array("O0A.pdb")
O0Glist = pdb2array("O0G.pdb")
O0Ilist = pdb2array("O0I.pdb")
O0Klist = pdb2array("O0K.pdb")
O0Nlist = pdb2array("O0N.pdb")
O0Elist = pdb2array("O0E.pdb")
H0Hlist = pdb2array("H0H.pdb")
H0Jlist = pdb2array("H0J.pdb")
H0Mlist = pdb2array("H0M.pdb")
H0Olist = pdb2array("H0O.pdb")
H0Flist = pdb2array("H0F.pdb")
O0Qlist = pdb2array("O0Q.pdb")
N0Ulist = pdb2array("N0U.pdb")
N0Rlist = pdb2array("N0R.pdb")
H0Wlist = pdb2array("H0W.pdb")
H0Vlist = pdb2array("H0V.pdb")
H0Tlist = pdb2array("H0T.pdb")
H0Slist = pdb2array("H0S.pdb")

OWHW1list = defdonor(OWlist,HW1list)
OWHW2list = defdonor(OWlist,HW2list)
O0EH0Flist = defdonor(O0Elist,H0Flist)
O0NH0Olist = defdonor(O0Nlist,H0Olist)
O0KH0Mlist = defdonor(O0Klist,H0Mlist)
O0IH0Jlist = defdonor(O0Ilist,H0Jlist)
O0GH0Hlist = defdonor(O0Glist,H0Hlist)
N0UH0Wlist = defdonor(N0Ulist,H0Wlist)
N0UH0Vlist = defdonor(N0Ulist,H0Vlist)
N0RH0Tlist = defdonor(N0Rlist,H0Tlist)
N0RH0Slist = defdonor(N0Rlist,H0Slist)

output1 = open("hbond-stat.txt", 'w')
output2 = open("hbond-stat-details.txt", 'w')
output1.write("%s %s %s %s %s %s\n" % ("frame","index","hb","hbgg","hbgw","hbgu"))
output2.write("%s %s %s %s %s %s\n" % ("frame","index","hb","hbgagd","hbgawd","hbgaud"))

for i in range(len(O0Alist)):
    for j in range(len(O0Alist[0])):
        x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
        if ((x2 > 2.0) and (x2 < 48.0) and (y2 > 2.0) and (y2 < 48.0) and (z2 > 2.0) and (z2 < 48.0)):
            hbgagd, hbgawd, hbgaud = 0, 0, 0
            hbgg, hbgw, hbgu = 0, 0, 0
            
            for k in range(len(O0IH0Jlist[0])):
                x1, y1, z1 = float(O0IH0Jlist[i][k][1][0]),float(O0IH0Jlist[i][k][1][1]), float(O0IH0Jlist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(O0IH0Jlist[i][k][0][0]),float(O0IH0Jlist[i][k][0][1]), float(O0IH0Jlist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgagd=hbgagd+1

            for k in range(len(O0EH0Flist[0])):
                x1, y1, z1 = float(O0EH0Flist[i][k][1][0]),float(O0EH0Flist[i][k][1][1]), float(O0EH0Flist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(O0EH0Flist[i][k][0][0]),float(O0EH0Flist[i][k][0][1]), float(O0EH0Flist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgagd=hbgagd+1                 

            for k in range(len(O0NH0Olist[0])):
                x1, y1, z1 = float(O0NH0Olist[i][k][1][0]),float(O0NH0Olist[i][k][1][1]), float(O0NH0Olist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(O0NH0Olist[i][k][0][0]),float(O0NH0Olist[i][k][0][1]), float(O0NH0Olist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgagd=hbgagd+1

            for k in range(len(O0GH0Hlist[0])):
                x1, y1, z1 = float(O0GH0Hlist[i][k][1][0]),float(O0GH0Hlist[i][k][1][1]), float(O0GH0Hlist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(O0GH0Hlist[i][k][0][0]),float(O0GH0Hlist[i][k][0][1]), float(O0GH0Hlist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgagd=hbgagd+1
            
            for k in range(len(O0KH0Mlist[0])):
                x1, y1, z1 = float(O0KH0Mlist[i][k][1][0]),float(O0KH0Mlist[i][k][1][1]), float(O0KH0Mlist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(O0KH0Mlist[i][k][0][0]),float(O0KH0Mlist[i][k][0][1]), float(O0KH0Mlist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgagd=hbgagd+1
                                                
            for k in range(len(OWHW1list[0])):
                x1, y1, z1 = float(OWHW1list[i][k][1][0]),float(OWHW1list[i][k][1][1]), float(OWHW1list[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(OWHW1list[i][k][0][0]),float(OWHW1list[i][k][0][1]), float(OWHW1list[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgawd=hbgawd+1
                        
            for k in range(len(OWHW2list[0])):
                x1, y1, z1 = float(OWHW2list[i][k][1][0]),float(OWHW2list[i][k][1][1]), float(OWHW2list[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(OWHW2list[i][k][0][0]),float(OWHW2list[i][k][0][1]), float(OWHW2list[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgawd=hbgawd+1                        
                        
            for k in range(len(N0UH0Wlist[0])):
                x1, y1, z1 = float(N0UH0Wlist[i][k][1][0]),float(N0UH0Wlist[i][k][1][1]), float(N0UH0Wlist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(N0UH0Wlist[i][k][0][0]),float(N0UH0Wlist[i][k][0][1]), float(N0UH0Wlist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgaud=hbgaud+1            
            
            for k in range(len(N0UH0Vlist[0])):
                x1, y1, z1 = float(N0UH0Vlist[i][k][1][0]),float(N0UH0Vlist[i][k][1][1]), float(N0UH0Vlist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(N0UH0Vlist[i][k][0][0]),float(N0UH0Vlist[i][k][0][1]), float(N0UH0Vlist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgaud=hbgaud+1
            
            for k in range(len(N0RH0Tlist[0])):
                x1, y1, z1 = float(N0RH0Tlist[i][k][1][0]),float(N0RH0Tlist[i][k][1][1]), float(N0RH0Tlist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(N0RH0Tlist[i][k][0][0]),float(N0RH0Tlist[i][k][0][1]), float(N0RH0Tlist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgaud=hbgaud+1
            
            for k in range(len(N0RH0Slist[0])):
                x1, y1, z1 = float(N0RH0Slist[i][k][1][0]),float(N0RH0Slist[i][k][1][1]), float(N0RH0Slist[i][k][1][2]) 
                x2, y2, z2 = float(O0Alist[i][j][0]), float(O0Alist[i][j][1]), float(O0Alist[i][j][2]) 
                x3, y3, z3 = float(N0RH0Slist[i][k][0][0]),float(N0RH0Slist[i][k][0][1]), float(N0RH0Slist[i][k][0][2]) 
                d23 = math.sqrt((x3-x2)**2. + (y3-y2)**2. + (z3-z2)**2.)
                if (d23 <= 3.5):
                    d13 = math.sqrt((x1-x3)**2. + (y1-y3)**2. + (z1-z3)**2.)
                    dotp = ((x1-x3)*(x2-x3) + (y1-y3)*(y2-y3) + (z1-z3)*(z2-z3))/(d23*d13)
                    if dotp >= 0.866:
                        hbgaud=hbgaud+1                                                
            
            hb = hbgagd + hbgawd + hbgaud
            hbgg = hbgagd
            hbgw = hbgawd
            hbgu = hbgaud
            
            output1.write("%d %d %d %d %d %d\n" % (i,j,hb,hbgg,hbgw,hbgu))
            output2.write("%d %d %d %d %d %d\n" % (i,j,hb,hbgagd,hbgawd,hbgaud))

output1.close()
output2.close()