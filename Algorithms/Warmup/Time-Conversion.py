#!/bin/python

import sys
time = raw_input().strip()

if time[-2:] == 'AM':
    if time[:2] == '12':
        time = '00' + time[2:-2]
    else:
        time = time[:-2]
elif time[-2:] == 'PM':
    if time[:2] == '12':
        time = time[:-2]
    else:
        time = str(int(time[:2])+12) + time[2:-2]
        
print time
