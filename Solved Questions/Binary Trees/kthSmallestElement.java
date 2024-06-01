import java.util.*;

class node {
    int data;
    node right;
    node left;

    node(int n) {
        data = n;
        right = null;
        left = null;
    }

}

public class kthSmallestElement {
    public static node built(int[] a) {
        if (a.length == 0)
            return null;
        node root = new node(a[0]);
        Queue<node> q = new LinkedList<>();
        q.add(root);
        int i=1;
        while (!q.isEmpty() && i < a.length) {
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
    
    public static int kthsmallest(node root, int k) {
        List<Integer> l = new ArrayList<>();
        inorder(root, l);
        if (l.size() < k) {
            return -1;
        }
        return l.get(k - 1);
    }

    public static void inorder(node root, List<Integer> l) {
        if (root == null)
            return;
        inorder(root.left, l);
        l.add(root.data);
        inorder(root.right, l);
    }
    
    public static void main(String[] args) {
        int[] a = { 3, 1, 4, -1, 2 }; // -1 means null
        node root = built(a);
        int k = 2;
        System.out.println(kthsmallest(root,k));
    }
}