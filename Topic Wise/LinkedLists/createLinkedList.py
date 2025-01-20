 # Single Linked List All Operations
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,x):
        if self.head is None:
            self.head=Node(x)
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=Node(x) # type: ignore

    def printList(self):
        cur=self.head
        res=[]
        while cur is not None:
            res.append(cur.val)
            cur=cur.next
        print("-->".join(map(str,res)))

    # Insert at beginnning
    def insertAtBegin(self,x):
        new_node=Node(x)
        new_node.next=self.head # type: ignore
        self.head=new_node

    # Insertion at a given position
    def insertAt(self,x,pos):
        cur=self.head
        for i in range(pos-1):
            cur=cur.next # type: ignore
        new_node=Node(x)
        new_node.next=cur.next # type: ignore
        cur.next=new_node # type: ignore

    # Insert at End
    def insertAtEnd(self,x):
        cur=self.head
        while cur.next is not None: # type: ignore
            cur=cur.next # type: ignore
        new_node=Node(x)
        cur.next=new_node # type: ignore
    
    # Deletion at beginning
    def deleteAtBegin(self):
        self.head=self.head.next # type: ignore

    # Deletion at end
    def deleteAtEnd(self):
        cur=self.head
        while cur.next.next is not None: # type: ignore
            cur=cur.next # type: ignore
        cur.next=None # type: ignore

    # Deletion at a given position
    def deleteAt(self,pos):
        cur=self.head
        for i in range(pos-1):
            cur=cur.next # type: ignore
        cur.next=cur.next.next # type: ignore

    # Deletion by value
    def deleteByValue(self,x):
        cur=self.head
        while cur.next.val!=x: # type: ignore
            cur=cur.next # type: ignore
        cur.next=cur.next.next # type: ignore


    # Reverse a linked list
    def reverse(self): # Iterative
        cur=self.head
        prev=None
        while cur is not None:
            next=cur.next
            cur.next=prev # type: ignore
            prev=cur
            cur=next
        
        self.head=prev

    # reverse a ll, recursive
    def reverseRecursive(self,cur,prev):
        if cur is None:
            self.head=prev
            return
        next=cur.next
        cur.next=prev
        self.reverseRecursive(next,cur)



arr=[1,2,3,4,5]
ll=LinkedList()
for i in arr:
    ll.insert(i)
ll.printList()
ll.insertAtBegin(0)
ll.insertAtEnd(6)
ll.printList()
ll.insertAt(3,2)
ll.printList()
ll.deleteAtBegin()
ll.printList()
ll.deleteAtEnd()
ll.printList()
ll.deleteAt(3)
ll.printList()
ll.deleteByValue(3)
ll.printList()
ll.reverse()
ll.printList()
ll.reverseRecursive(ll.head,None)
ll.printList()