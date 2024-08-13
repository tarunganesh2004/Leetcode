// Bottom View of Binary Tree
import java.util.*;

class node {
    int data;
    node left;
    node right;

    node(int n) {
        data = n;
        left = null;
        right = null;
    }
}

class pair {
    node n;
    int hd;

    pair(node n, int hd) {
        this.n = n;
        this.hd = hd;
    }
}

class bottomview {
    public static node buildTree(int[] a) {
        if (a.length == 0 || a[0] == -1) {
            return null;
        }
        node root = new node(a[0]);
        Queue<node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (i < a.length) {
            node cur = q.poll();
            if (a[i] != -1) {
                cur.left = new node(a[i]);
                q.add(cur.left);
            }
            i++;
            if (i < a.length && a[i] != -1) {
                cur.right = new node(a[i]);
                q.add(cur.right);
            }
            i++;
        }
        return root;
    }

    public static List<Integer> bv(node root) {
        List<Integer> l = new ArrayList<>();
        if (root == null) {
            return l;
        }
        TreeMap<Integer, Integer> m = new TreeMap<>();
        Queue<pair> q = new LinkedList<>();
        q.add(new pair(root, 0));
        while (!q.isEmpty()) {
            pair p = q.poll();
            node cur = p.n;
            int hd = p.hd;

            m.put(hd, cur.data);
            if (cur.left != null) {
                q.add(new pair(cur.left, hd - 1));
            }
            if (cur.right != null) {
                q.add(new pair(cur.right, hd + 1));
            }
        }
        for (int i : m.values()) {
            l.add(i);
        }
        return l;
    }

    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 10, 9, 11, -1, 5, -1, -1, -1, -1, -1, -1, -1, 6 };
        node root = buildTree(a);
        List<Integer> ans = bv(root);
        for (int i : ans) {
            System.out.print(i + " ");
        }
    }
}