def ransom_note(magazine, ransom):
    # construct two dicts
    magDict = {}
    for word in magazine:
        magDict[word] = magDict.get(word,0)+1
    ransomDict = {}
    for word in ransom:
        ransomDict[word] = ransomDict.get(word,0)+1
    
    for word in ransomDict:
        if magDict.get(word,0) < ransomDict[word]:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
