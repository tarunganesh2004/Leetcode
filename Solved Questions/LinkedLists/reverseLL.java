class node {
    int data;
    node next;

    node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class reverseLL {
    static node head;

    public static node insert(node head, int data) {
        if (head == null)
            return new node(data);
        else {
            node cur = head;
            while (cur.next != null) {
                cur = cur.next;
            }
            cur.next = new node(data);
        }
        return head;
    }

    public static void print(node head) {
        node cur = head;
        while (cur != null) {
            System.out.print(cur.data + " ");
            cur = cur.next;
        }
        System.out.println();
    }

    public static node reverseIterative(node head) {
        node prev = null;
        node cur = head;
        node next = null;
        while (cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    // Recursive
    public static node reverseRecursive(node head) {
        if (head == null || head.next == null)
            return head;
        node newHead = reverseRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return newHead;
    }

    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5 };
        node head = null;
        for (int i = 0; i < a.length; i++) {
            head = insert(head, a[i]);
        }

        // Reverse using iterative approach
        head = reverseIterative(head);
        System.out.print("Iteratively reversed list: ");
        print(head);

        // Reverse again using recursive approach
        head = reverseRecursive(head);
        System.out.print("Recursively reversed list: ");
        print(head);
    }
}
