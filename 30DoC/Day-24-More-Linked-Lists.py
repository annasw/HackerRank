class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

# this is the method i wrote
    def removeDuplicates(self,head):
        if head == None: return head
        if head.next == None: return head
        
        datas = [head.data]
        trueHead = head
        nextNode = head.next
        while nextNode != None:
            if nextNode.data in datas:
                head.next = nextNode.next
                nextNode = head.next
            else:
                datas.append(nextNode.data)
                head = head.next
                nextNode = head.next
        return trueHead

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

