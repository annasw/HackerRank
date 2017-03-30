# doesn't work yet; needs correction

# we need to check for nonadjacent swaps

n = int(raw_input())
array = map(int, raw_input().split(" "))

works = True
lPointer = 0
rPointer = 0
if len(array)>1:
    for index in range(0,len(array)-1):
        if array[index]>array[index+1]:
            if lPointer==rPointer==0:
                lPointer = index
                rPointer = index+1
            elif index-rPointer>0:
                works = False
                break
            else:
                rPointer = index+1

# check to see if it works
#print "original array",array
if not lPointer==rPointer==0:
    array = array[0:lPointer]+array[lPointer:rPointer+1][::-1]+array[rPointer+1:len(array)]
    #print "constructed array",array
    if array != sorted(array):
        #print "pointers",lPointer, rPointer
        #print "sorted", sorted(array)
        works = False

if works:
    print "yes"
    if lPointer==rPointer==0:
        pass
    elif rPointer-lPointer>1:
        print "reverse", lPointer+1, rPointer+1
    else:
        print "swap", lPointer+1, rPointer+1
else:
    print "no"
    
