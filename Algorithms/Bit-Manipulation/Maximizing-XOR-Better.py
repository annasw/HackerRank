#!/bin/python

# significantly better solution

def maxXOR(left, right):
    i = left^right
    n = 0
    while i:
        n+=1
        i = i>>1
    return 2**n-1

left = int(raw_input())
right = int(raw_input())
print maxXOR(left, right)
