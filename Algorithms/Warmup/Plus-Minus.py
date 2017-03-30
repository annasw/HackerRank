#!/bin/python

# i'm legitimately upset that the only way (i've found) to get custom precision on a decimal in python
# is by importing the decimal module AND using its quantize method
# AND using another freaking Decimal as an argument in said method

import sys
from decimal import *

n = Decimal(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = Decimal(0)
neg = Decimal(0)
zero = Decimal(0)
for x in arr:
    if x>0: pos+=1
    elif x<0: neg+=1
    else: zero+=1

print (pos/n).quantize(Decimal(10)**-6)
print (neg/n).quantize(Decimal(10)**-6)
print (zero/n).quantize(Decimal(10)**-6)
