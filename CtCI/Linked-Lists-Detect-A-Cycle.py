"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# returns a boolean: TRUE if there is a cycle, FALSE otherwise.
# first implementation; the list of vals is unnecessary and we can do with just a list of pointers,
# but doesn't matter at this scale.
# also inefficient
def has_cycle(head):
    if head == None: return False
    elif head.next == None: return False
    vals = []
    pointers = []
    while head.next != None:
        h = head.data
        if h in vals:
            if head in pointers:
                return True
            pointers.append(head)
        vals.append(h)
        head = head.next
    return False

