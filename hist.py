# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 14:29:43 2021

@author: UnseR
"""
import numpy as np
import matplotlib.pyplot as plt
a=[]
f=open("poiss.dat")
for i in f:
    a.append(i)
f.close()
a1=np.asarray(a)
plt.hist(a1,10,density=True)