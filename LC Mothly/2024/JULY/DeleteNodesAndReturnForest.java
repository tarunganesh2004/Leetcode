import java.util.*;

class Node {
    int val;
    Node left;
    Node right;

    Node(int n) {
        val = n;
        left = null;
        right = null;
    }
}

public class DeleteNodesAndReturnForest {
    public static Node buildTree(Integer[] a) {
        if (a.length == 0 || a[0] == null)
            return null;
        Node root = new Node(a[0]);
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while (i < a.length) {
            Node cur = q.poll();
            if (a[i] != null) {
                cur.left = new Node(a[i]);
                q.add(cur.left);
            }
            i++;
            if (i < a.length && a[i] != null) {
                cur.right = new Node(a[i]);
                q.add(cur.right);
            }
            i++;
        }
        return root;
    }

    public static List<Node> delNodes(Node root, int[] toDelete) {
        Set<Integer> s = new HashSet<>();
        for (int i : toDelete) {
            s.add(i);
        }
        List<Node> res = new ArrayList<>();
        root = process(root, s, res);
        if (root != null) {
            res.add(root);
        }
        return res;
    }

    public static Node process(Node cur, Set<Integer> s, List<Node> l) {
        if (cur == null)
            return null;
        cur.left = process(cur.left, s, l);
        cur.right = process(cur.right, s, l);
        if (s.contains(cur.val)) {
            if (cur.left != null) {
                l.add(cur.left);
            }
            if (cur.right != null) {
                l.add(cur.right);
            }
            return null;
        }
        return cur;
    }

    public static void printTree(Node root) {
        if (root == null) {
            System.out.println("null");
            return;
        }
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            System.out.print(node.val + " ");
            if (node.left != null) {
                queue.add(node.left);
            }
            if (node.right != null) {
                queue.add(node.right);
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Integer[] a = { 1, 2, 4,null,3 };
        int[] toDelete = { 3 };
        Node root = buildTree(a);
        List<Node> res = delNodes(root, toDelete);
        for (Node n : res) {
            printTree(n);
        }
    }
}
