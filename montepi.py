# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:55:59 2020

@author: Alienware
"""

import numpy as np
#numero de pruebas
import matplotlib.pyplot as plt
import time

n=[1000, 10000, 100000, 1000000]

error=[]
tiempo=[]

for i in n:
    t1=time.time()
    j= np.random.random((i, 2))   
    z= np.sqrt(j[:,0]*j[:,0]+j[:,1]*j[:,1])
    condi1=z<1
    bb=condi1.sum()
    pi= 4*bb/i
    error.append(100*abs(pi-np.pi)/np.pi)
    t2=time.time()
    tiempo.append(t2-t1)
    a1=np.ma.masked_where(z<1, z)
    a2=np.ma.masked_where(z>=1, z)
    plt.scatter(j[:,0], j[:,1], s=a1)
    plt.scatter(j[:,0], j[:,1], s=a2)