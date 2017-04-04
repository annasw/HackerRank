# i wrote most of the class, not the top-level code

class MyQueue(object):
    def __init__(self):
        self.inbox = []
        self.outbox = []
    
    def fillOutbox(self):
        if not self.inbox:
            raise IndexError('Tried to fill outbox without anything in inbox')
        else:
            while self.inbox:
                self.outbox.append(self.inbox[-1])
                self.inbox = self.inbox[:-1]
    
    def peek(self):
        if not self.outbox:
            self.fillOutbox()
        return self.outbox[-1]
        
    def pop(self):
        if not self.outbox:
            self.fillOutbox()
        r = self.outbox[-1]
        self.outbox = self.outbox[:-1]
        return r
        
    def put(self, value):
        self.inbox.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
