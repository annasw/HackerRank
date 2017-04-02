n = int(raw_input())
maxLen = 0
currLen = 0
while n:
    if n%2==1:
        currLen+=1
    else:
        maxLen = max(maxLen, currLen)
        currLen = 0
    n>>=1
maxLen = max(maxLen, currLen)
print maxLen
