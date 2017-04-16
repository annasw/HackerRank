import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    # this is what I wrote
    def levelOrder(self,root):
        if root == None or root == []: # not sure what an empty tree looks like
            return
        
        queue = [root]
        while queue:
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)
            print(root.data,end=' ')
            
            # move to the next elt in the queue
            queue = queue[1:]
            root = queue[0]
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
