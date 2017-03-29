# for this challenge, we're using a hashtable (python dict) instead of a sparse array

n = int(raw_input())
d = {}
for x in range(n):
    s = raw_input()
    d[s] = d.get(s,0)+1

q = int(raw_input())
for x in range(q):
    query = raw_input()
    print d.get(query,0)
