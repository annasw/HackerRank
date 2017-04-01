#!/bin/python

import sys

def lonely_integer(a):
    i = 0
    for x in a:
        i ^= x
    return i

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
