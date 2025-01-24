# Delete the Middle Node of a Linked List LC 2095

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def insert(self,data):
        if self.head is None:
            self.head=ListNode(data)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=ListNode(data)
    
    def printll(self):
        res=[]
        temp=self.head
        while temp is not None:
            res.append(temp.val)
            temp=temp.next
        print("->".join(map(str,res)))

    def deleteMiddle(self):
        # edge case
        if not self.head or not self.head.next:
            return None
        slow=self.head
        fast=self.head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next # type: ignore
            fast=fast.next.next 
        prev.next=slow.next # type: ignore
        return self.head
    
ll=LinkedList()
arr=[1,3,4,7,1,2,6]
for i in arr:
    ll.insert(i)
ll.deleteMiddle()
ll.printll()