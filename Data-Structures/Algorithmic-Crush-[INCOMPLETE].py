# works in general, but not for obnoxious gigantic test cases
# doesn't yet pass all the HackerRank test cases

n, m = map(int, raw_input().split(" "))
ls = dict([(x+1,0) for x in range(n)])
for o in range(m):
    a,b,k = map(int, raw_input().split(" "))
    for idx in range(a,b+1):
        ls[idx]+=k

print max(ls.values())
