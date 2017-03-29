# basically just borrowed from my answer to what is effectively the same problem in the CtCI category

n, d = map(int, raw_input().split(" "))
array = map(int, raw_input().split(" "))

first = array[:d%n]
second = array[d%n:]
for x in first:
    second.append(x)
for x in second:
    print x,
