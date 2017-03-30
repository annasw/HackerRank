n = int(raw_input())

for x in range(n):
    s = raw_input()
    print ''.join([s[i] for i in range(0,len(s)) if i%2==0]), ''.join([s[i] for i in range(0,len(s)) if i%2==1])
