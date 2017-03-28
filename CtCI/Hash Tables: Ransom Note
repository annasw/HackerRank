# working version, this one in python

def ransom_note(magazine, ransom):
    magHash = {}
    ransomHash = {}
    
    for x in magazine:
        if x in magHash:
            magHash[x] = magHash.get(x)+1
        else:
            magHash[x] = 1
    
    for x in ransom:
        if x in ransomHash:
            ransomHash[x] = ransomHash.get(x)+1
        else:
            ransomHash[x] = 1
    
    # this iterator is completely unnecessary
    # (and awkward; why do Python iterators NEED to throw an exception? cmon)
    '''
    i = iter(ransomHash)
    try:
        while(True):
            e = i.next()
            if e not in magHash or ransomHash[e] > magHash[e]:
                return False
    except StopIteration:
        return True
    '''
    # MUCH better (and more pythonic) implementation:
    for x in ransomHash:
        if x not in magHash or ransomHash[x]>magHash[x]:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
