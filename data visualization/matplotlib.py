#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:11:06 2021

@author: lucasdonaire
"""

import numpy as np
import matplotlib.pyplot as plt
import math


x= np.linspace(-1, 1, 2000)

y = x**2

plt.figure()
plt.plot(x,y,'bh',label='e**x sinx',linewidth= 1.1)
plt.legend()


#### subplots

import matplotlib.pyplot as plt
fig,a =  plt.subplots(2,2)
import numpy as np



fig.suptitle('Grid de 4 plots - by me')
fig.dpi=80 
fig.facecolor = 'y'
a[0][0].plot(x,y*y)
a[0][0].set_title('Square')

a[0][1].plot(x,np.sqrt(y))
a[0][1].set_title('Square root')

a[1][0].plot(x,np.exp(y))
a[1][0].set_title('Exp')

a[1][1].plot(x,np.log10(y))
a[1][1].set_title('Log')

plt.show()