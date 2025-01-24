# Add Two Numbers LC 2

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = ListNode(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = ListNode(data) # type: ignore
    
    def printll(self):
        res=[]
        temp = self.head
        while temp is not None:
            res.append(temp.val)
            temp = temp.next
        print("->".join(map(str,res)))

    def addTwoNumbers(self,l1,l2):
        dummy=ListNode(0)
        cur=dummy
        carry=0
        while l1 or l2:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            sum=x+y+carry
            carry=sum//10
            cur.next=ListNode(sum%10) # type: ignore
            cur=cur.next # type: ignore
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            cur.next=ListNode(1) # type: ignore
        self.head=dummy.next
        return self.head
        

l1=LinkedList()
arr1=[9,9,9,9,9,9,9]
for i in arr1:
    l1.insert(i)
l2=LinkedList()
arr2=[9,9,9,9]
for i in arr2:
    l2.insert(i)

l3=LinkedList()
l3.addTwoNumbers(l1.head,l2.head)
l3.printll()