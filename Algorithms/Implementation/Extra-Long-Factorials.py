#!/bin/python

import sys

n = int(raw_input().strip())
d = 1

while n>0:
    d*=n
    n-=1

print d
