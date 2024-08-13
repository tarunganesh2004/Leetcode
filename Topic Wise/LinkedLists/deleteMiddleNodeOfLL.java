// LC 2095 Delete the Middle Node of a Linked List

class node {
    int data;
    node next;

    node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class deleteMiddleNodeOfLL {
    static node head;

    public static node insert(node head, int data) {
        if (head == null) {
            return new node(data);
        } else {
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

    public static node deleteMiddle(node head) {
        if(head==null|| head.next==null) return null;
        node slow = head;
        node fast = head.next;
        while (fast != null && fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        slow.next = slow.next.next;
        return head;
    }
    public static void main(String[] args) {
        int[] a = { 1, 3, 4, 7, 1, 2, 6 };
        for (int i = 0; i < a.length; i++) {
            head = insert(head, a[i]);
        }
        node res = deleteMiddle(head);
        print(res);
    }
}
