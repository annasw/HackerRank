# i implemented my own Stack class for OOP practice
class Stack:
    def __init__(self):
        self.maxes = []
        self.stack = []
    
    def push(self, elt):
        self.stack.append(elt)
        if not self.maxes or elt>self.maxes[-1]:
            self.maxes.append(elt)
        else:
            self.maxes.append(self.maxes[-1])
    
    def pop(self):
        self.maxes = self.maxes[:-1]
        self.stack = self.stack[:-1]

    def maxElt(self):
        return self.maxes[-1]

s = Stack()
n = int(raw_input())
for x in range(n):
    q = raw_input()
    if str(q[0])=='1':
        s.push(int(q[2:]))
    elif str(q[0])=='2':
        s.pop()
    elif str(q[0])=='3':
        print s.maxElt()
    
    
