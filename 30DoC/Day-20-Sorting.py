#!/bin/python3

import sys

def bubbleSort(ls):
    totalSwaps = 0
    while True:
        numSwaps = 0
        for i in range(len(ls)-1):
            if ls[i]>ls[i+1]:
                temp = ls[i]
                ls[i] = ls[i+1]
                ls[i+1] = temp
                numSwaps += 1
                totalSwaps += 1
        if numSwaps == 0:
            break
    return [ls, totalSwaps]


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
results = bubbleSort(a)

print("Array is sorted in %d swaps." % results[1])
print("First Element: %d" % results[0][0])
print("Last Element: %d" % results[0][-1])
