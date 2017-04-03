# working implementation of something that is not an insertion sort

#!/bin/python
def insert(elt, ar):
    if elt>ar[-1]:
        ar.append(elt)
        return ar
    elif elt<ar[0]:
        ls = [elt]
        for x in arr: ls.append(x)
        return ls
    for x in range(len(ar)):
        if ar[x]>elt:
            ls = ar[:x]
            ls.append(elt)
            for i in ar[x:]:
                ls.append(i)
            return ls

def insertionSort(array):    
    newList = [array[0]]
    array=array[1:]
    for x in array:
        newList = insert(x,newList)
        for i in newList: print i,
        print "\n",
    #print newList

m = input()
array = [int(i) for i in raw_input().strip().split()]
insertionSort(array)
