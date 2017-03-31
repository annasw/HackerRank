#!/bin/python

import sys

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# complete honesty, i straight up forgot to check this the first time and got a divide-by-zero
if v1==v2: print 'NO'
else:
    t = (x2-x1+0.0)/(v1-v2)
    if t>0 and int(t)==t:
        print 'YES'
    else: print 'NO'
