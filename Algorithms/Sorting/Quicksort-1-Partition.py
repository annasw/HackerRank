n = int(raw_input())
array = map(int, raw_input().strip().split(' '))

left = []
equal = []
right = []
pivot = array[0]
for i in array:
    if i<pivot: left.append(i)
    elif i==pivot: equal.append(i)
    elif i>pivot: right.append(i)
for i in left: print i,
for i in equal: print i,
for i in right: print i,
