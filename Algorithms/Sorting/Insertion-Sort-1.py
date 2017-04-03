n = int(raw_input())
arr = map(int, raw_input().strip().split(' '))
temp = arr[-1]

for i in range(len(arr)-2,-1,-1):
    if arr[i]>temp:
        arr[i+1]=arr[i]
        for x in arr: print x,
        print "\n",
    else:
        arr[i+1]=temp
        for x in arr: print x,
        break
    if i==0:
        arr[i] = temp
        for x in arr:print x,
