# Convert Binary Number in a Linked List to Integer LC 1290


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node # type: ignore


class Solution:
    def getDecimalValue(head): # type: ignore
        binary_str = ""
        cur = head
        while cur is not None:
            binary_str += str(cur.val) # type: ignore
            cur = cur.next # type: ignore
        return int(binary_str, 2)


arr = [1, 0, 1]
ll = LinkedList()
for i in arr:
    ll.insert(i)

print(Solution.getDecimalValue(ll.head))  # type: ignore # Output: 5
