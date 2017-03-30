#!/bin/python

# perhaps not algorithmically optimal, but we're dealing with five numbers here

import sys

ls = map(long, raw_input().strip().split(' '))
ls = sorted(ls)
print sum(ls[:-1]),sum(ls[1:])
