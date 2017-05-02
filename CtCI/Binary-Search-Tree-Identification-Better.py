# significantly cleaner and more functional implementation

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
# importing inf lets us start with lo and hi outside any possible finite value of the tree,
# rather than having to start with fixed limits or figure them out beforehand.
from math import inf

# we use optional arguments to avoid the need to write a second method
def check_binary_search_tree_(root, lo=-inf, hi=inf):
    # and we check None here to avoid the need to check awkwardly on the initial call and each recursive call.
    if root==None: return True
    if root.data >= hi or root.data <= lo: return False

    return check_binary_search_tree_(root.left, lo, root.data) and check_binary_search_tree_(root.right, root.data, hi)
