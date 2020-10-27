# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:55:59 2020

@author: Alienware
"""

import numpy as np
#numero de pruebas
import matplotlib.pyplot as plt
from time import time

n=np.logspace(2,6,4)
n=np.abs(n)
plt.plot(n)
plt.grid()

error=[]
tiempo=[]


plt.figure(figsize=(15,15))

for k,i in enumerate(n):
    t1=time()
    j= np.random.random((int(i), 2))   
    z= np.sqrt(j[:,0]*j[:,0]+j[:,1]*j[:,1])
    condi1=z<1
    bb=condi1.sum()
    pi= 4*bb/i
    error.append(100*abs(pi-np.pi)/np.pi)
    t2=time()
    tiempo.append(t2-t1)
    a1=np.ma.masked_where(z<1, z)
    a2=np.ma.masked_where(z>=1, z)
    plt.subplot(2,2,k+1)
    plt.scatter(j[:,0], j[:,1], s=a1)
    plt.scatter(j[:,0], j[:,1], s=a2)
plt.show()

