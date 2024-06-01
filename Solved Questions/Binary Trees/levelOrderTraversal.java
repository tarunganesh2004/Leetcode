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
public class levelOrderTraversal {
    public static node built(int[] a) {
        if (a.length == 0)
            return null;
        node root = new node(a[0]);
        Queue<node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
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

    public static List<List<Integer>> levelOrder(node root) {
        List<List<Integer>> l = new ArrayList<>();
        if (root == null) {
            return l;
        }
        Queue<node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            // node cur = q.poll();
            List<Integer> a = new ArrayList<>();
            int c = q.size();
            for (int i = 0; i < c; i++) {
                node cur = q.poll();
                a.add(cur.data);
                if (cur.left != null) {
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                }

            }
            l.add(a);
        }
        return l;
    }

    // Another Approach
    public static List<List<Integer>> lo(node root) {
        List<List<Integer>> l = new ArrayList<>();
        if (root == null) {
            return null;
        }
        helper(root, 0, l);
        return l;
    }

    public static void helper(node root,int level,List<List<Integer>> list){
        if (root == null)
            return;
        if (level == list.size()) {
            List<Integer> newList = new ArrayList<>();
            newList.add(root.data);
            list.add(newList);
        } else {
            list.get(level).add(root.data);
        }
        helper(root.left, level + 1, list);
        helper(root.right, level + 1, list);
        return;
    }

    public static void main(String[] args) {
        int[] a = { 3, 9, 20, -1, -1, 15, 7 };
        node root = built(a);
        List<List<Integer>> l = lo(root);
        List<List<Integer>> l1 = BottomUplevelOrder(root);
        System.out.println(l);
        System.out.println(l1);
    }

    // Bottom up level order levelOrderTraversal
    public static List<List<Integer>> BottomUplevelOrder(node root) {
        List<List<Integer>> l = new ArrayList<>();
        if (root == null) {
            return l;
        }
        Queue<node> q = new LinkedList<>();
        Stack<List<Integer>> s = new Stack<>();
        q.add(root);
        while (!q.isEmpty()) {
            // node cur = q.poll();
            List<Integer> a = new ArrayList<>(); // current level
            int c = q.size();
            for (int i = 0; i < c; i++) {
                node cur = q.poll();
                a.add(cur.data);
                if (cur.left != null) {
                    q.add(cur.left);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                }

            }
            s.push(a);
        }
        while (!s.isEmpty()) {
            l.add(s.pop());
        }
        return l;
    }
}
