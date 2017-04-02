#!/bin/python

import sys

def getExpectation(ch):
    if ch=='[':
        return ']'
    if ch=='{':
        return '}'
    if ch=='(':
        return ')'

leftBrackets = ['[','(','{']
rightBrackets = [']',')','}']

n = int(raw_input())
for x in range(n):
    expectations = []
    s = raw_input()
    result = "YES"
    if len(s)<2:
        result = "NO"
    else:
        while s:
            if s[0] in leftBrackets:
                expectations.append(getExpectation(s[0]))
            else: # s[0] in rightBrackets
                if not expectations or s[0]!=expectations[-1]:
                    result = "NO"
                    break
                else: # match
                    expectations = expectations[:-1] # pop the last expectation
            s = s[1:]
    
    if expectations:
        result = "NO"
    print result
