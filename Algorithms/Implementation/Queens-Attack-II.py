#!/bin/python

import sys

# n = sidelength, k = num obstacles
n,k = map(int, raw_input().strip().split(' '))
rQueen, cQueen = map(int, raw_input().strip().split(' '))

# distance from queen to edge of board (or obstacle)
distTop = n-rQueen
distBot = n-distTop-1
distRight = n-cQueen
distLeft = n-distRight-1
distTR = min(distRight,distTop)
distTL = min(distTop,distLeft)
distBR = min(distBot,distRight)
distBL = min(distBot,distLeft)

for i in range(k):
    r, c = map(int, raw_input().strip().split(' '))
    
    # find which direction the given obstacle (at r,c) falls into
    vDiff = r-rQueen
    hDiff = c-cQueen
    if abs(vDiff)==abs(hDiff): # diagonal
        if vDiff>0: # above
            if hDiff>0: # top right
                distTR = min(distTR,vDiff-1)
            else: # top left
                distTL = min(distTL,vDiff-1)
        else: # below
            if hDiff>0: # bottom right
                distBR = min(distBR,hDiff-1)
            else: # bottom left
                distBL = min(distBL,abs(hDiff)-1)
    elif vDiff==0: # same row
        if hDiff>0:
            distRight = min(distRight,hDiff-1)
        else: # hDiff<0
            distLeft = min(distLeft,-1*hDiff-1)
    elif hDiff==0: # same column
        if vDiff>0:
            distTop = min(distTop,vDiff-1)
        else: #vDiff<0
            distBot = min(distBot,-1*vDiff-1)
    
    # otherwise it's not relevant
    
print distTop+distBot+distLeft+distRight+distTR+distBR+distBL+distTL
