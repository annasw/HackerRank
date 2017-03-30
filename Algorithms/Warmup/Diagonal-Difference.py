#!/bin/python

import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

diagA = 0
diagB = 0

for i in range(len(a)):
    diagA += a[i][i]
    diagB += a[i][len(a)-i-1]

print abs(diagA-diagB)
