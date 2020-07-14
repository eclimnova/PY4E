# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
#tuples lesson

x, y = 3, 4
print(y)

days = ('Mon', 'Tue', 'Wed') 
print(days[2])


c = {'a':10, 'd':1, 'c':22}
print(c.items())
t = (sorted(c.items()))

print(t)
print(type(c))

tmp = list()
for k, v in c.items() :
    newtup = (v,k)
    tmp.append(newtup) 
tmp = sorted(tmp, reverse=True)
for val, key in tmp[:1] :
     print(key, val)

f = {'a':10, 'b':1, 'c':22}
print(sorted( [ (v,k) for k,v in f.items() ], reverse=True)) 

import numpy as np
import pandas as pd
