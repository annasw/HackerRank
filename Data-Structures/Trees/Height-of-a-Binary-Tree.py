class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# this is the only method i wrote
def height(root):
    def recurse(root,h):
        if root.left!=None or root.right!=None:
            h+=1
            if root.right==None:
                return recurse(root.left, h)
            elif root.left==None:
                return recurse(root.right, h)
            else:
                return max(recurse(root.left,h),recurse(root.right,h))
        else:
            return h
    h = 0
    return recurse(root,h)
    
    

tree = BinarySearchTree()
t = int(raw_input())

for _ in xrange(t):
    x = int(raw_input())
    tree.create(x)

print height(tree.root)
