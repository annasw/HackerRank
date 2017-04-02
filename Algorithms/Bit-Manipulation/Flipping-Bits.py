n = int(raw_input())
for x in range(n):
    i = int(raw_input())
    print i^4294967295 # i.e. 2**32-1, or 32 1s in binary. this flips every bit of i.
    
