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

public class findLargestInEachRow {
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
    public static List<Integer> findLargest(node root) {
        List<Integer> l = new ArrayList<>();
        if (root == null)
            return l;
        Queue<node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int size = q.size();
            int max = Integer.MIN_VALUE;
            for (int i = 0; i < size; i++) {
                node cur = q.poll();
                max = Math.max(max, cur.data);
                if (cur.left != null)
                    q.add(cur.left);
                if (cur.right != null)
                    q.add(cur.right);

            }
            l.add(max);
        }
        return l;
    } 
    public static void main(String[] args) {
        Integer[] a = { 1, 3, 2, 5, 3, null, 9 };
        node root = buildTree(a);
        System.out.println(findLargest(root));
    }
}
