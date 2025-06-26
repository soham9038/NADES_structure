import os
#list1=[]
#list2=[]
def defdonor(list1,list2):
    lista = []
    listc = {}
    s=-1
    for i in range(len(list1)):
        s=s+1
        t=-1
        listb={}
        for j in range(len(list1[0])):
            t=t+1
            lista = []
            lista.append(list1[i][j])
            lista.append(list2[i][j])
            #print(i, j)
            listb[t]=lista
        
        listc[s]=listb
      
    return listc
