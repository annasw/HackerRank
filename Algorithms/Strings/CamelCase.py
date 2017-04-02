#!/bin/python

import sys
import string

s = raw_input().strip()

count = 1
uc = string.uppercase
for x in s:
    if x in uc:
        count+=1
print count
