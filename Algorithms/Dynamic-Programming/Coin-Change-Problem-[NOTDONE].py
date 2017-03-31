# this isn't even at the testing stage yet
# i'm just saving it here so it doesn't get deleted from hackerrank

d = {}

# takes a goal number and a list of coins,
# returns number of ways to make change for goal with coins
def makeChange(goal, ls):
    if goal==0:
        return 1
    elif goal<ls[0]:
        d[goal] = 0
        return 0
    if goal in d:
        return d.get(goal)
    ways = 0
    for i in ls:
        if i<=goal:
            if goal-i in d:
                ways += d[goal-i]
            else:
                temp = makeChange(goal-i, ls)
                
        else:
            break
    
    
    return ways
    


# n = amount to make change for, m = number of types of coins
n,m = map(int, raw_input().strip().split(' '))
coins = map(int, raw_input().strip().split(' '))

if n==0:
    ans = 0
elif len(coins)==0:
    ans = 0
else:
    ans = makeChange(n,sorted(coins))
print ans
