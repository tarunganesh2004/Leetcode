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

public class evenOddTree {
    public static node buildTree(Integer[] a) {
        if (a.length == 0 || a[0] == null) {
            return null;
        }
        node root = new node(a[0]);
        Queue<node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (i < a.length) {
            node cur = q.poll();
            if (a[i] != null) {
                cur.left = new node(a[i]);
                q.add(cur.left);
            }
            i++;
            if (i < a.length && a[i] != null) {
                cur.right = new node(a[i]);
                q.add(cur.right);
            }
            i++;
        }
        return root;
    }

    public static boolean isEvenOddTree(node root) {
        if (root == null)
            return true;
        Queue<node> q = new LinkedList<>();
        q.add(root);
        int n = 0;
        while (!q.isEmpty()) {
            int s = q.size();
            List<Integer> k = new ArrayList<>();
            for (int i = 0; i < s; i++) {
                node cur = q.poll();
                k.add(cur.data);
                if (cur.left != null) {
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                }
            }

            if (n % 2 == 0) {
                if (!isOdd(k) || !increasing(k)) {
                    return false;
                }
            } else {
                if (!isEven(k) || !decreasing(k)) {
                    return false;
                }
            }
            n++;
        }
        return true;
    }

    public static boolean isOdd(List<Integer> l) {
        for (int i = 0; i < l.size(); i++) {
            if (l.get(i) % 2 == 0) {
                return false;
            }
        }
        return true;
    }
    
    public static boolean isEven(List<Integer> l) {
        for (int i = 0; i < l.size(); i++) {
            if (l.get(i) % 2 == 1) {
                return false;
            }
        }
        return true;
    }

    public static boolean increasing(List<Integer> l) {
        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) >= l.get(i + 1)) {
                return false;
            }
        }
        return true;
    }

    public static boolean decreasing(List<Integer> l) {
        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) <=l.get(i + 1)) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        Integer[] a = { 5,4,2,3,3,7};
        node root = buildTree(a);
        System.out.println(isEvenOddTree(root));
    }
}
