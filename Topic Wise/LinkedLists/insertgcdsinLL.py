# Insert Greatest Common Divisor (GCD) in a Linked List LC 2807

import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = ListNode(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = ListNode(data)
    def printll(self):
        res = []
        temp = self.head
        while temp is not None:
            res.append(temp.val)
            temp = temp.next
        print("->".join(map(str, res)))

class Solution:
    def insertGCD(self,head):
        if head is None or head.next is None:
            return head
        
        n1=head
        n2=head.next 
        while n2 is not None:
            gcd=math.gcd(n1.val, n2.val)
            new_node = ListNode(gcd)
            n1.next= new_node
            new_node.next = n2

            n1 = n2
            n2 = n2.next
        return head
    
arr=[18,6,10,3]
ll=LinkedList()
for i in arr:
    ll.insert(i)
sol=Solution()
sol.insertGCD(ll.head)
ll.printll()