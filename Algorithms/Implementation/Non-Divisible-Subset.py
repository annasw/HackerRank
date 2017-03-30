'''
I'm actually pretty proud of this one. The problem was to determine the maximum size of a subset
of integers in a list such that no two integers summed to a number divisible by a given integer k.
The math trick is to realize that (a+b)%k==0 iff a%k+b%k==0.
Which means:

1. If we have any numbers n s.t. n%k==0, we can use exactly one of them;
2. If we have any numbers m s.t. m%k==k/2 (if k is even), we can use exactly one of them;
3. For any other remainder i<k, there is a corresponding j<k s.t. i+j==k (and thus if we have
n and m s.t. n%k==i and m%k==j, then k|n+m).

So we use a dict to store our remainders in key-value pairs where the key is the remainder of n%k for all n in the list
and the value is the number of times that remainder has occurred. Then we check all those of remainder r
s.t. r!=0 and r!=k/2 (excepting (1) and (2) above) to see which of the pair of i and j had more numbers
in our set. The larger total gets added. We do this for all i (and corresponding j) less than k/2.
'''

import math

# dict of (remainder, count) for modulo k
d = {}

# n = number of integers in the list, k = divisor
n,k = map(int, raw_input().strip().split(' '))

# list of integers
s = map(int, raw_input().strip().split(' '))

for i in s:
    d[i%k] = d.get(i%k,0)+1

maxSubset = 0
if d.get(0,0)>0:
    maxSubset+=1
if k%2==0 and d.get(k/2,0)>0:
    maxSubset+=1
for v in range(1, int(math.ceil(k/2.))):
    maxSubset += max(d.get(v,0),d.get(k-v,0))

print maxSubset
