n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def bubbleSort(array):
    numSwaps,totSwaps = 0,0
    
    while True:
        for idx in range(len(array)-1):
            if array[idx]>array[idx+1]:
                x = array[idx]
                array[idx]=array[idx+1]
                array[idx+1]=x
                numSwaps+=1
                totSwaps+=1
        if numSwaps == 0:
            break
        else:
            numSwaps = 0
    
    print "Array is sorted in %i swaps." % totSwaps
    print "First Element: %i" % array[0]
    print "Last Element: %i" % array[-1]

bubbleSort(a)
