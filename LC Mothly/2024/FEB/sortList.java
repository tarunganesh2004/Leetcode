class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class sortList {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0)
            return head;

        ListNode tail = head;
        int len = 1;
        while (tail.next != null) {
            tail = tail.next;
            len++;
        }
        if (len == 1 || k % len == 0)
            return head;

        if (k > len) {
            k = k % len;
        }
        ListNode newLast = head;
        for (int i = 0; i < len - k - 1; i++) {
            newLast = newLast.next;
        }

        ListNode newHead = newLast.next;
        newLast.next = null;
        tail.next = head;
        head = newHead;
        return head;
    }

    // Utility method to print the linked list
    public void printList(ListNode node) {
        while (node != null) {
            System.out.print(node.val + " ");
            node = node.next;
        }
        System.out.println();
    }

    // Method to create a linked list from an array
    public ListNode createList(int[] arr) {
        if (arr == null || arr.length == 0)
            return null;
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }

    public static void main(String[] args) {
        sortList solution = new sortList();

        // Test case 1
        int[] arr1 = { 1, 2, 3, 4, 5 };
        ListNode head1 = solution.createList(arr1);
        int k1 = 2;
        System.out.println("Original list:");
        solution.printList(head1);
        ListNode rotatedHead1 = solution.rotateRight(head1, k1);
        System.out.println("List after rotating right by " + k1 + " places:");
        solution.printList(rotatedHead1);

        // Test case 2
        int[] arr2 = { 0, 1, 2 };
        ListNode head2 = solution.createList(arr2);
        int k2 = 4;
        System.out.println("\nOriginal list:");
        solution.printList(head2);
        ListNode rotatedHead2 = solution.rotateRight(head2, k2);
        System.out.println("List after rotating right by " + k2 + " places:");
        solution.printList(rotatedHead2);
    }
}
