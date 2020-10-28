# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:55:59 2020

@author: Alienware
"""

import numpy as np
#numero de pruebas
import matplotlib.pyplot as plt
<<<<<<< HEAD:MC simple/montepi.py
import time

n=[1000, 10000, 100000, 1000000]
=======
from time import time

n=np.logspace(2,6,4)
n=np.abs(n)
plt.plot(n)
plt.grid()
>>>>>>> 3ec36c1598104ba794f285ebf39da47bb2026af1:monte carlo simple/montepi.py

error=[]
tiempo=[]

<<<<<<< HEAD:MC simple/montepi.py
for i in n:
    t1=time.time()
    j= np.random.random((i, 2))   
=======

plt.figure(figsize=(15,15))

for k,i in enumerate(n):
    t1=time()
    j= np.random.random((int(i), 2))   
>>>>>>> 3ec36c1598104ba794f285ebf39da47bb2026af1:monte carlo simple/montepi.py
    z= np.sqrt(j[:,0]*j[:,0]+j[:,1]*j[:,1])
    condi1=z<1
    bb=condi1.sum()
    pi= 4*bb/i
    error.append(100*abs(pi-np.pi)/np.pi)
<<<<<<< HEAD:MC simple/montepi.py
    t2=time.time()
    tiempo.append(t2-t1)
    a1=np.ma.masked_where(z<1, z)
    a2=np.ma.masked_where(z>=1, z)
    plt.scatter(j[:,0], j[:,1], s=a1)
    plt.scatter(j[:,0], j[:,1], s=a2)
=======
    t2=time()
    tiempo.append(t2-t1)
    a1=np.ma.masked_where(z<1, z)
    a2=np.ma.masked_where(z>=1, z)
    plt.subplot(2,2,k+1)
    plt.scatter(j[:,0], j[:,1], s=a1)
    plt.scatter(j[:,0], j[:,1], s=a2)
plt.show()

>>>>>>> 3ec36c1598104ba794f285ebf39da47bb2026af1:monte carlo simple/montepi.py
