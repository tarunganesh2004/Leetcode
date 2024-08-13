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

public class viewsOfTrees {
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

    public static List<Integer> leftView(node root) {
        List<Integer> l = new ArrayList<>();
        if (root == null)
            return l;
        lv(root, 0, l);
        return l;
    }
    public static void lv(node root, int level, List<Integer> l) {
        if (root == null)
            return;
        if (l.size() == level) {
            l.add(root.data);

        }
        lv(root.left, level + 1, l);
        lv(root.right, level + 1, l);
    }
    public static List<Integer> rightView(node root) {
        List<Integer> l = new ArrayList<>();
        if (root == null)
            return l;
        rv(root, 0, l);
        return l;
    }

    public static void rv(node root, int level, List<Integer> l) {
        if (root == null)
            return;
        if (l.size() == level) {
            l.add(root.data);

        }
        rv(root.right, level + 1, l);
        rv(root.left, level + 1, l);
    }

    public static void main(String[] args) {
        Integer[] a={1,2,3,null,5,null,4};
        node root = buildTree(a);
        List<Integer> r = rightView(root);
        List<Integer> l = leftView(root);
        System.out.println(r);
        System.out.println(l);
    }
}
