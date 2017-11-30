# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 13:43:06 2017

@author: Syamsul
"""

import csv
import numpy

f1 = open('dataCurah.csv')
csvf_1 = csv.reader(f1)

n = []
#print(n)
for row in csvf_1:
    #print(row[2])
    n.append(row)

ndata = len(n)
#print(ndata)

#membuat array count nya..
R = [0,0,0]
S = [0,0,0]
T = [0,0,0]

Rtotal = [0,0,0]
Stotal = [0,0,0]
Ttotal = [0,0,0]
for i in range(0,ndata-1):
    if(n[i] == ['Rendah']):
        if(n[i+1] == ['Rendah']):
            R[0]=R[1]+1
        elif(n[i+1] == ['Sedang']):
            R[1]+=1
        elif(n[i+1] == ['Tinggi']):
            R[2]+=1
    elif(n[i] == ['Sedang']):
        if(n[i+1] == ['Rendah']):
            S[0]+=1
        elif(n[i+1] == ['Sedang']):
            S[1]+=1
        elif(n[i+1] == ['Tinggi']):
            S[2]+=1
    elif(n[i] == ['Tinggi']):
        if(n[i+1] == ['Rendah']):
            T[0]+=1
        elif(n[i+1] == ['Sedang']):
            T[1]+=1
        elif(n[i+1] == ['Tinggi']):
            T[2]+=1    

print("   R   S   T")
print("R",R)
print("S",S)
print("T",T)

"""
for i in range(0,2):
    Rtotal[i]=R[i]/ndata
    Stotal[i]=S[i]/ndata
    Ttotal[i]=T[i]/ndata


print("   R   S   T")
print("R",Rtotal)
print("S",Stotal)
print("T",Ttotal)
"""