#!/bin/python

import sys

q = int(raw_input().strip())

for x in range(q):
    ballDict = {} # keys: ball types (0 thru n-1), vals: # of balls of that type
    bucketDict = {} # keys: # of balls in bucket. Vals: # of buckets of that size

    n = int(raw_input().strip())
    for r in range(n):
        line = map(int, raw_input().strip().split(' '))
        s = sum(line)
        bucketDict[s] = bucketDict.get(s,0)+1
        
        for i in range(n):
            ballDict[i] = ballDict.get(i,0)+line[i]

    vals = ballDict.values()
    for v in vals:
        bucketDict[v] = bucketDict.get(v,0)-1

    results = bucketDict.values()
    text = "Possible"
    for x in results:
        if x<0:
            text = "Impossible"
            break
    print text
