#!/bin/python

import sys

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apples = map(int,raw_input().strip().split(' '))
oranges = map(int,raw_input().strip().split(' '))

appleDistance = s-a
orangeDistance = t-b
houseWidth = t-s
appleCount = 0
orangeCount = 0
for x in apples:
    if x>=appleDistance and x<=appleDistance+houseWidth: appleCount+=1
for y in oranges:
    if y<=orangeDistance and y>=orangeDistance-houseWidth: orangeCount+=1

print appleCount
print orangeCount
