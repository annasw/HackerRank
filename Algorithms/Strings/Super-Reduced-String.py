def reduceString(s):
    if len(s)==0: return 'Empty String'
    elif len(s)==1: return s
    
    idxA = 0
    idxB = 1

    while True:
        if s[idxA]==s[idxB]:
            s = s[:idxA] + s[idxB+1:]
            if len(s)<2: break
            idxA,idxB=0,1
                
        else:
            if idxB >= len(s)-1:
                break
            else:
                idxA,idxB = idxB,idxB+1
    if len(s)==0: s = 'Empty String'
    return s

def main():
    s = raw_input().strip()
    print reduceString(s)

if __name__=="__main__":
    main()
