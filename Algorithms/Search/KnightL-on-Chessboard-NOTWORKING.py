'''
Doesn't work yet.
Didn't finish implementing it.
'''

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
    
    def eltInQueue(self, elt):
        if not self.outbox:
            self.fillOutbox()
        return elt in self.outbox



# positions are stored as a triple: (x-coordinate, y-coordinate, depth-in-search)
def bfs(a,b,lasPos):
    if x+a<n:
        if y+b<n:
            e = (x+a,y+b,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
        if y-b>=0:
            e = (x+a,y-b,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
    if x-a>=0:
        if y+b<n:
            e = (x-a,y+b,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
        if y-b>=0:
            e = (x-a,y-b,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
    if x+b<n:
        if y+a<n:
            e = (x+b,y+a,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
        if y-a>=0:
            e = (x+b,y-a,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
    if x-b>=0:
        if y+a<n:
            e = (x-b,y+a,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
        if y-a>=0:
            e = (x-b,y-a,lastPos[2]+1)
            if not moves.eltInQueue(e):
                moves.put(e)
    
    #for
    



moves = MyQueue() # declare new in each for loop
n = int(raw_input())


