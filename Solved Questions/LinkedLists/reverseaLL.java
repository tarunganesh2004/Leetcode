class node {
    int data;
    node next;
    node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class reverseaLL {
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
    }

    public static node reverse(node head) {
        node prev = null;
        node cur = head;
        node next = head;
        while (cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5 };
        node head = null;
        for (int i = 0; i < a.length; i++) {
            head = insert(head, a[i]);
        }
        head = reverse(head);
        print(head);
    }
}
