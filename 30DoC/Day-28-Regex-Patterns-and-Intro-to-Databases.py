#!/bin/python3

import sys
import re


N = int(input().strip())
names = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    p = re.compile('.*@gmail\.com$')
    if p.match(emailID)!=None: names.append(firstName)

for n in sorted(names): print(n)
    
