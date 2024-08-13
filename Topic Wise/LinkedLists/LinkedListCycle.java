class node {
    int data;
    node next;
    node(int data) {
        this.data = data;
        this.next = null;
    }

}

class LinkedListCycle {
    static node head;

    static node insert(node head, int data) {
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

    public static boolean hasCycle(node head) {
        node slow = head;
        node fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }

        }
        return false;
    }
    public static void main(String[] args) {
        int[] a = { 3, 2, 0, -4 };
        for (int i = 0; i < a.length; i++) {
            head = insert(head, a[i]);
        }
        
        System.out.println(hasCycle(head));
    }
}