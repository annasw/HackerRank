# The challenge was to get this as efficient as possible.
# This runs in O(.5*n^(1/2)), which is of course O(n^(1/2)) but with a good coefficient.
# The only way I can think of to make it faster would be to reference a list of known primes,
# but that's neither convenient nor all that helpful (it's just a slightly better constant).

from math import sqrt

def isPrime(n):
    if n==1: return False
    if n==2 or n==3 or n==5: return True
    if n%2==0: return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0: return False
    return True

def main():
    t = int(input())
    for test in range(t):
        num = int(input())
        if isPrime(num): print("Prime")
        else: print("Not prime")

if __name__=="__main__":
    main()
    
