# A recursive implementation of Fibonacci.
# The iterative one actually works better.

# This also uses DP, storing Fib values in a dict.
# Thus it works better for a large number of queries (because DP),
# but fails with large fib indices (because recursion).

# Data: for 100,000 queries (from 0-1000), on my machine
# the iterative Fib runs in about 10.6 seconds; recursive Fib in 0.03.
# But the threshold for recursive failure is somewhere between f(1000) and f(2000).

fibDict = {0:0, 1:1}

def fibonacci(n):
    if n in fibDict: return fibDict[n]
    
    result = 0
    if n-1 not in fibDict: fibDict[n-1] = fibonacci(n-1)
    result += fibDict[n-1]
    
    if n-2 not in fibDict: fibDict[n-2] = fibonacci(n-2)
    result += fibDict[n-2]
    
    return result
    
n = int(input())
print(fibonacci(n))
