# Remove Nth Node from End of List LC 19

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        if self.head is None:
            self.head=ListNode(data)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=ListNode(data) # type: ignore
    
    def printll(self):
        res=[]
        temp=self.head
        while temp is not None:
            res.append(temp.val)
            temp=temp.next
        print("->".join(map(str,res)))

    def removeNthFromEnd(self,head,n):
        dummy=ListNode(0)
        dummy.next=head
        first=dummy
        second=dummy
        for _ in range(n):
            first=first.next # type: ignore
        if first is None:
            return self.head.next # type: ignore
        while first.next is not None:
            first=first.next
            second=second.next # type: ignore
        second.next=second.next.next # type: ignore
        # self.head=dummy.next
        return self.head
    
    

arr=[1,2,3,4,5]
n=2
ll=LinkedList()
for i in arr:
    ll.insert(i)

ll.removeNthFromEnd(ll.head,n)
ll.printll()