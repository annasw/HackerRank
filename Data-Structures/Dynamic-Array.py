n, q = map(int, raw_input().split(" "))

seqList = []
for x in range(n):
    seqList.append([])

lastAns = 0

for x in range(q):
    query = map(int, raw_input().split(" "))
    i = (query[1]^lastAns)%n
    if query[0]==1:
        seqList[i].append(query[2])
    if query[0]==2:
        lastAns = seqList[i][query[2]%len(seqList[i])]
        print lastAns
