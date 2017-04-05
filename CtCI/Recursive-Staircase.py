# keys: num of stairs, values: ways to climb
d = {0:1}
stepOptions = [3,2,1]

def waysToClimb(n):
    ways = 0
    for step in stepOptions:
        if step<=n:
            if n-step in d:
                ways+=d[n-step]
            else:
                temp = waysToClimb(n-step)
                d[n-step] = temp
                ways += temp
    return ways

s = int(raw_input())
for i in range(s):
    numStairs = int(raw_input())
    print waysToClimb(numStairs)
