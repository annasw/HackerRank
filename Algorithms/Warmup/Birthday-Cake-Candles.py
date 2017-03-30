#!/bin/python

import sys

n = int(raw_input().strip())
heights = map(int,raw_input().strip().split(' '))

d = {}

for h in heights:
    d[h] = d.get(h,0)+1

m = max(d.keys())
print d[m]
