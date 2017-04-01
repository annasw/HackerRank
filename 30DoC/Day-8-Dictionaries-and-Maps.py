n = int(raw_input())
d = {}
for x in range(n):
    a,b = raw_input().strip().split(' ')
    d[a]=b

try:
    while True:
        q = raw_input().strip()
        if q in d:
            print q+'='+d[q]
        else:
            print "Not found"
except:
    pass
    
