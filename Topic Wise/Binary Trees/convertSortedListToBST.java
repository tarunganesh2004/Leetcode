// LC 109 

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}
class node{
    int val;
    node left;
    node right;
    node(int x){
        val = x;
        left = null;
        right = null;
    }
}

class convertSortedListToBST {
    static ListNode head = null;
    
    // Linkedlist insertion
    public static void insert(int x) {
        ListNode cur = new ListNode(x);
        if (head == null) {
            head = cur;
        } else {
            ListNode temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = cur;
        }
        // return cur;

    }

    public static node convert(ListNode head) {
        List<Integer> l = new ArrayList<>();
        ListNode cur = head;
        while (cur != null) {
            l.add(cur.val);
            cur = cur.next;
        }
        // return l;
        node r = convertListToBST(l, 0, l.size() - 1);
        return r;
    }
    public static node convertListToBST(List<Integer> l, int start, int end) {
        if (start > end) {
            return null;
        }
        int mid = (start + end) / 2;
        node root = new node(l.get(mid));
        root.left = convertListToBST(l, start, mid - 1);
        root.right = convertListToBST(l, mid + 1, end);
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            insert(sc.nextInt());
        }
        node root = convert(head);
        System.out.println(root.val);
        sc.close();
    }
}