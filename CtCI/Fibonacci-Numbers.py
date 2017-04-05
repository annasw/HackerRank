def fibonacci(n):
    fibA = 0
    fibB = 1
    for x in range(n-1):
        fibA,fibB = fibB,fibA+fibB
    return fibB

n = int(raw_input())
print(fibonacci(n))
