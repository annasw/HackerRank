# This problem has "Binary Search" in the title, but a binary search makes no sense here.
# This data isn't sorted... Meaning anything binary search runs in O(nlogn)
# So instead I did two non-binary-search solutions.

# a naive search method (O(n**2))
def naiveSearch(m,a):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]+a[j] == m:
                return [i+1,j+1]

# and a sophisticated hashmap search method (O(n))
def sophisticatedHashMapSearch(m,a):
    d = {} # keys: price, values: index
    for idx in range(len(a)): # indices in a
        diff = m-a[idx]
        if diff in d:
            return [d[diff],idx+1] # we're iterating in order, so the earlier idx is in the dict
        else:
            d[a[idx]] = idx+1 # insert idx into dict (1-indexing)
            # note that we don't need to check for repeats, since either
            # A) a[idx]*2 == m, in which case there's no repeat (or else we would have found it as d[diff]), or
            # B) a[idx]*2 != m, in which case a repeated value CAN'T be part of a unique solution.

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip()) # amount of money
    n = int(input().strip()) # number of flavors of ice cream
    a = list(map(int, input().strip().split(' '))) # list of ice cream prices
    
    for elt in sophisticatedHashMapSearch(m,a): print(elt, end=' ')
    print()
