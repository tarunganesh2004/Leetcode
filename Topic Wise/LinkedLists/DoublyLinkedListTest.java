class DoublyNode {
    int data;
    DoublyNode next;
    DoublyNode prev;

    DoublyNode(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class DoublyLinkedListTest {
    static DoublyNode head;

    // Insert at the end of the list
    public static DoublyNode insertAtEnd(DoublyNode head, int data) {
        DoublyNode newNode = new DoublyNode(data);
        if (head == null) {
            return newNode;
        }
        DoublyNode cur = head;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.next = newNode;
        newNode.prev = cur;
        return head;
    }

    // Insert at a specific position
    public static DoublyNode insertAtPosition(DoublyNode head, int data, int position) {
        DoublyNode newNode = new DoublyNode(data);
        if (position == 0) { // Insert at the head
            newNode.next = head;
            if (head != null) {
                head.prev = newNode;
            }
            return newNode;
        }
        DoublyNode cur = head;
        for (int i = 0; i < position - 1 && cur != null; i++) {
            cur = cur.next;
        }
        if (cur == null) {
            System.out.println("Position out of bounds");
            return head;
        }
        newNode.next = cur.next;
        newNode.prev = cur;
        if (cur.next != null) {
            cur.next.prev = newNode;
        }
        cur.next = newNode;
        return head;
    }

    // Delete at a specific position
    public static DoublyNode deleteAtPosition(DoublyNode head, int position) {
        if (head == null) {
            System.out.println("List is empty");
            return null;
        }
        if (position == 0) { // Delete the head node
            if (head.next != null) {
                head.next.prev = null;
            }
            return head.next;
        }
        DoublyNode cur = head;
        for (int i = 0; i < position && cur != null; i++) {
            cur = cur.next;
        }
        if (cur == null) {
            System.out.println("Position out of bounds");
            return head;
        }
        if (cur.next != null) {
            cur.next.prev = cur.prev;
        }
        if (cur.prev != null) {
            cur.prev.next = cur.next;
        }
        return head;
    }

    // Delete at the end of the list
    public static DoublyNode deleteAtEnd(DoublyNode head) {
        if (head == null) {
            System.out.println("List is empty");
            return null;
        }
        if (head.next == null) { // Only one node in the list
            return null;
        }
        DoublyNode cur = head;
        while (cur.next != null) {
            cur = cur.next;
        }
        cur.prev.next = null; // Remove the last node
        return head;
    }

    // Reverse the doubly linked list
    public static DoublyNode reverse(DoublyNode head) {
        DoublyNode temp = null;
        DoublyNode cur = head;
        while (cur != null) {
            temp = cur.prev;
            cur.prev = cur.next;
            cur.next = temp;
            cur = cur.prev;
        }
        if (temp != null) {
            head = temp.prev;
        }
        return head;
    }

    // Print the doubly linked list
    public static void printList(DoublyNode head) {
        DoublyNode cur = head;
        while (cur != null) {
            System.out.print(cur.data + " <-> ");
            cur = cur.next;
        }
        System.out.print("null\n");
    }

    public static void main(String[] args) {
        // Insert elements at the end
        int[] a = { 1, 2, 3, 4, 5 };
        for (int i = 0; i < a.length; i++) {
            head = insertAtEnd(head, a[i]);
        }
        System.out.println("Original List:");
        printList(head);

        // Insert at a specific position
        head = insertAtPosition(head, 6, 2);
        System.out.println("After inserting 6 at position 2:");
        printList(head);

        // Delete at a specific position
        head = deleteAtPosition(head, 3);
        System.out.println("After deleting at position 3:");
        printList(head);

        // Delete at end
        head = deleteAtEnd(head);
        System.out.println("After deleting at end:");
        printList(head);

        // Reverse the list
        head = reverse(head);
        System.out.println("Reversed List:");
        printList(head);
    }
}
