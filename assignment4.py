# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:10:27 2021

@author: Swapnil Sirsat
"""

import numpy as np
import matplotlib.pyplot as plt
import math
#the three equations of the line would be as
# x = y
# y = 0
# root(3)y + 7 = x
Y = [4,3,2,1,0]
X = []
for i in Y:
    X.append((-math.sqrt(3))*i +7)

#
plt.plot([0,1,2,3,4,5,6,7],[0, 0 , 0 , 0 , 0 , 0 , 0,0],color = 'red')
plt.plot([0,1,2,3,4,5],[0,1,2,3,4,5])
plt.plot(X,Y)
plt.show()
