#!/bin/python

import sys
import math

s = ''.join(raw_input().strip().split(' '))

# first we determine the number of rows and columns
L = len(s)
f,c = map(int, (math.floor(math.sqrt(L)), math.ceil(math.sqrt(L))))
rows,columns = 0,0
if f*f>=L:
    rows,columns = f,f
elif f*c>=L:
    rows,columns = f,c
else:
    rows,columns = c,c

# now we populate the 2d array (maybe unnecessary, maybe not)
array = [[] for x in range(rows)]

for x in range(rows-1):
    for i in range(columns):
        array[x].append(s[0])
        s = s[1:]
while s:
    array[rows-1].append(s[0])
    s = s[1:]

# now we make an array of words... carefully
words = ['' for x in range(columns)]
for x in range(columns):
    for i in range(rows-1):
        words[x] = words[x]+array[i][x]
for e in range(len(array[rows-1])):
    words[e] = words[e] + array[rows-1][e]

for x in words:
    print x,
