""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def recursiveCheck(root, minVal, maxVal):
    if root.data<=minVal or root.data>=maxVal:
        return False
    b = True
    if root.left!=None:
        b = recursiveCheck(root.left,minVal,root.data)
    if root.right!=None and b:
        b = recursiveCheck(root.right,root.data,maxVal)
    return b

def check_binary_search_tree_(root):
    if root==None:
        return True
    else:
        # 0<=val<=10**4
        return recursiveCheck(root,-1,10001)
