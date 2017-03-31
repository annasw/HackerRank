# takes a string word
# returns "no answer" if word is lexicographically maximized
# else returns the next biggest lexicographic arrangement of word
# (z>y>x>...>b>a>9>...)
def nextBiggest(word):
    letters = ''
    while word:
        newLetter = word[-1]
        word = word[:-1]
        bigger = []
        for x in letters:
            if x>newLetter:
                bigger.append(x)
        if bigger: # if there's a letter bigger than newLetter
            big = min(bigger)
            word = word + big
            #letters = ''.join(list(letters).remove(big))
            l = list(letters + newLetter)
            l.remove(big)
            for i in sorted(l):
                word = word + i
            return word
        else: # there is no bigger letter
            letters = newLetter + letters
    return "no answer" # the word is already maximized

n = int(raw_input())

for t in range(n):
    print nextBiggest(raw_input())
