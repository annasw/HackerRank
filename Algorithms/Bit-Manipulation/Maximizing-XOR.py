# slow, unclever O(n**2) solution

#!/bin/python

def maxXOR(left, right):
    currMax = 0
    for x in range(left,right):
        for y in range(x+1,right+1):
            currMax = max(currMax,x^y)
    return currMax

left = int(raw_input())
right = int(raw_input())
print maxXOR(left, right)
