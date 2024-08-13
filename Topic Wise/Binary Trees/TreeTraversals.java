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

class TreeTraversals {
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

    public static List<Integer> inordertraversal(node root) {
        List<Integer> l = new ArrayList<>();
        inorder(root, l);
        return l;
    }

    public static void inorder(node root, List<Integer> l) {
        if (root == null)
            return;
        inorder(root.left, l);
        l.add(root.data);
        inorder(root.right, l);
    }

    public static List<Integer> preordertraversal(node root) {
        List<Integer> l = new ArrayList<>();
        preorder(root, l);
        return l;
    }

    public static void preorder(node root, List<Integer> l) {
        if (root == null)
            return;
        l.add(root.data);
        preorder(root.left, l);
        preorder(root.right, l);
    }
    
    public static List<Integer> postordertraversal(node root) {
        List<Integer> l = new ArrayList<>();
        postorder(root, l);
        return l;
    }
    public static void postorder(node root, List<Integer> l) {
        if (root == null)
            return;
        postorder(root.left, l);
        postorder(root.right, l);
        l.add(root.data);
    }
    public static void main(String[] args) {
        Integer[] a={1,null,2,3};
        node root = buildTree(a);
        List<Integer> l1 = inordertraversal(root);
        List<Integer> l2 = preordertraversal(root);
        List<Integer> l3 = postordertraversal(root);

        System.out.println("Inorder Traversal " + l1);
        System.out.println("Preorder Traversal " + l2);
        System.out.println("Postorder Traversal " + l3);
        
    }
}