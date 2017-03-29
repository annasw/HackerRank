# sort of badly explained (why are the variable names different here and in the problem description??)
# but i'm pretty sure n is the number of integers, k is the number of rotations, a is the list/array
# i tried a failed version with actual rotations before I figured out you can just do it all at once (also modulo)
def array_left_rotation(a, n, k):
    first = a[:k%n]
    second = a[k%n:]
    for e in first:
        second.append(e)
    return second

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
