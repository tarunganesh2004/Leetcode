import java.util.LinkedList;
import java.util.*;
class node {
    int data;
    node left;
    node right;

    node(int data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class stepbystepDirectionsFromBinaryTreeNodeToAnother {
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

    // public static node insert(node root, int data) {
    //     if (root == null) {
    //         return new node(data);
    //     }
    //     if (data < root.data) {
    //         root.left = insert(root.left, data);
    //     } else {
    //         root.right = insert(root.right, data);
    //     }
    //     return root;
    // }

    public static String getDirections(node root, int startValue, int destValue) {
        StringBuilder start = new StringBuilder();
        StringBuilder dest = new StringBuilder();
        find(root, startValue, start);
        find(root, destValue, dest);
        start.reverse();
        dest.reverse();
        while (start.length() > 0 && dest.length() > 0 && start.charAt(0) == dest.charAt(0)) {
            start.deleteCharAt(0);
            dest.deleteCharAt(0);
        }
        return "U".repeat(start.length()) + dest.toString();
    }

    public static boolean find(node root, int val, StringBuilder sb) {
        if (root == null) {
            return false;
        }
        if (root.data == val) {
            return true;
        }
        if (root.left != null && find(root.left, val, sb)) {
            sb.append("L");
            return true;
        }
        if (root.right != null && find(root.right, val, sb)) {
            sb.append("R");
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Integer[] a = { 5, 1, 2, 3, null, 6, 4 };
        int startValue = 3;
        int destValue = 6;
        node root = buildTree(a);
        String path = getDirections(root, startValue, destValue);
        System.out.println(path);
    }
}
