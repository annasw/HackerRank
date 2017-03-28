from string import ascii_lowercase

def number_needed(a, b):
    total = 0
    for c in ascii_lowercase:
        total += abs(a.count(c)-b.count(c))
    return total
    

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
