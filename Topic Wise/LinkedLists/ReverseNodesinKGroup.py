# Reverse Nodes in k-Group LC 25
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

    # Recursive approach
    def reverseKGroup(self,head,k):
        # Base case
        if head is None:
            return None
        if k==1:
            return head
        
        # count the number of nodes
        c=0
        temp=head
        while temp is not None:
            c+=1
            temp=temp.next
        if c<k:
            return head
        
        # reverse k nodes
        prev,cur=None,head
        for _ in range(k):
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node

        # recursively reverse next groups and connect
        head.next=self.reverseKGroup(cur,k)

        # return new head of the reversed group
        return prev
    
    # Iterative approach
    def reverseKGroupIterative(self,head,k):
        if not head or k==1:
            return head
        # count the number of nodes
        c=0
        temp=head
        while temp is not None:
            c+=1
            temp=temp.next
        if c<k:
            return head
        # initialise dummy node and pointers
        dummy=ListNode(0)
        dummy.next=head
        prev_group_end=dummy
        cur=head

        # reverse nodes in groups of k
        while c>=k:
            prev=None
            first=cur # 1st node of cur k-group

            # reverse k nodes
            for _ in range(k):
                next_node=cur.next
                cur.next=prev
                prev=cur
                cur=next_node
            # connect the reversed group to the previous group
            prev_group_end.next=prev # previs the new head of this k-group
            first.next=cur # first is now the last node of this k-group

            # move prev_group_end forward
            prev_group_end=first
            c-=k # reduce the remaining node count
        return dummy.next
    
ll = LinkedList()
arr=[1,2,3,4,5]
k=2
for i in arr:
    ll.insert(i)
ll.printll()
ll.head=ll.reverseKGroup(ll.head,k)
ll.printll()
ll.head=ll.reverseKGroupIterative(ll.head,k)
ll.printll()