from math import sqrt

def isPrime(n):
    if n==1: return "Not prime"
    elif n==2: return "Prime"
    elif n%2==0: return "Not prime"
    for i in range(3, int(sqrt(n)+3), 2):
        if n%i==0:
            return "Not prime"
    return "Prime"

p = int(raw_input())
for n in range(p):
    q = int(raw_input())
    print isPrime(q)
