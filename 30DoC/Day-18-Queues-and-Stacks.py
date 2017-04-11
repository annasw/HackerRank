import sys

# this problem is trivially solvable in O(n) with O(1) additional space
# point at the beginning and end of the string
# while the elts at each pointer agree, increment/decrement the pointers
# continue until they meet/pass.
class Solution:
    def __init__(self):
        self.stack = []
        self.queue = [] # ugh O(n) dequeueing complexity unless i build my own class (which i'm not doing)
    
    def pushCharacter(self, char):
        self.stack.append(char)
    
    def enqueueCharacter(self, char):
        self.queue.append(char)

    def popCharacter(self):
        topChar = self.stack[-1]
        self.stack = self.stack[0:-1]
        return topChar
    
    def dequeueCharacter(self):
        frontChar = self.queue[0]
        self.queue = self.queue[1:]
        return frontChar
        
# read the string s
s=raw_input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    
    
        
