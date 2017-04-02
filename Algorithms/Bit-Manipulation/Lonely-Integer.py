#!/usr/bin/py
# basically the same as the one from /CtCI

def lonelyInteger(a):
    i = 0
    for x in a:
        i ^= x
    return i

def main():
    n = int(raw_input())
    a = map(int, raw_input().strip().split(' '))
    print lonelyInteger(a)
    
if __name__=='__main__':
    main()
