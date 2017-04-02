#!/bin/python

# algorithm:
# - find the number of 0s in n; call this k
# - the number of possibilities is 2^k

def numZeros(n):
    count = 0
    while n:
        if n%2==0:
            count+=1
        n >>= 1
    return count

def sumVsXOR():
    i = int(raw_input())
    if i==0:
        print 1
    else:
        k = numZeros(i)
        print 2**k
    
sumVsXOR()
