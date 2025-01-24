# Convert Sorted List to Binary Search Tree LC 109

class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

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

    def sortedListToBST(self,head):
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow=head
        fast=head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None # type: ignore
        root=TreeNode(slow.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(slow.next)
        return root
    
class BST:
    def __init__(self):
        self.root=None
    
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

arr=[-10,-3,0,5,9]
ll=LinkedList()
for i in arr:
    ll.insert(i)

bst=BST()
bst.root=ll.sortedListToBST(ll.head) # type: ignore
bst.inorder(bst.root)