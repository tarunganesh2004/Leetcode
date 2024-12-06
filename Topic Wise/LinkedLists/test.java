class node {
    int data;
    node next;

    node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class test {
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

    public static node insertAt(node head, int data, int position) {
        node newNode = new node(data);
        if (position == 0) {
            newNode.next = head;
            return newNode;
        } else {
            node cur = head;
            for (int i = 0; i < position - 1; i++) {
                cur = cur.next;
            }
            if (cur == null) {
                System.out.println("Position out of bounds");
                return head;
            }
            newNode.next = cur.next;
            cur.next = newNode;
        }
        return head;
    }

    public static node deleteAt(node head, int data, int p) {
        if (head == null) {
            return null;
        }
        if (p == 0) {
            return head.next;
        } else {
            node cur = head;
            for (int i = 0; i < p - 1 && cur.next != null; i++) {
                cur = cur.next;
            }
            if (cur.next == null) {
                return head;
            }
            cur.next = cur.next.next;

        }
        return head;
    }

    public static node deleteAtEnd(node head) {
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return null;
        }
        else {
            node cur = head;
            while (cur.next != null) {
                cur = cur.next;
            }
            cur.next = null;
        }
        return head;

    }
    public static node reverse(node head) {
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
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5 };
        for (int i = 0; i < a.length; i++) {
            head = insert(head, a[i]);
        }
        // node cur = head;
        node head1 = insertAt(head, 4, 1);
        head1 = deleteAt(head, 4, 1);
        node cur = head;
        while (cur != null) {
            System.out.print(cur.data + "->");
            cur = cur.next;
        }
        System.out.print("null");
    }
}
