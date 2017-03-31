#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for x in range(len(arr)-1,-1,-1):
    print arr[x],
