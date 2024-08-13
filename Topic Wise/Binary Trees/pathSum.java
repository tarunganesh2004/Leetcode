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
public class pathSum {
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

    // find all paths from root to leaf sum equal to target
    // iterative solution
    public static List<List<Integer>> findPaths(node root, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null)
            return res;

        List<Integer> path = new ArrayList<>();
        Stack<node> st = new Stack<>();
        int pathsum = 0;
        node prev = null;
        node cur = root;

        while (cur != null || !st.isEmpty()) {
            while (cur != null) {
                st.push(cur);
                path.add(cur.data);
                pathsum += cur.data;
                cur = cur.left;
            }

            cur = st.peek();

            if (cur.right != null && cur.right != prev) {
                cur = cur.right;
                continue;
            }

            if (cur.left == null && cur.right == null && pathsum == target) {
                res.add(new ArrayList<>(path));
            }

            st.pop();
            pathsum -= cur.data;
            path.remove(path.size() - 1);
            prev = cur;
            cur = null;
        }
        return res;
    }
    
    // Recursive Approach
    public static List<List<Integer>> findPathsRecursive(node root, int target) {
        List<List<Integer>> l = new ArrayList<>();
        if (root == null)
            return l;
        find(root, target, l, new ArrayList<>());
        return l;
    }

    public static void find(node root, int target, List<List<Integer>> l, List<Integer> k) {
        if (root == null)
            return;
        k.add(root.data);
        if (root.left == null && root.right == null && root.data == target) {
            l.add(new ArrayList<>(k));
        }
        find(root.left, target - root.data, l, k);
        find(root.right, target - root.data, l, k);
        k.remove(k.size()-1);
    }

    public static boolean hasPathSum(node root,int target){
        if (root == null)
            return false;
        if (root.left == null && root.right == null && root.data - target == 0) {
            return true;
        }
        return hasPathSum(root.left, target - root.data) || hasPathSum(root.right, target - root.data);
    }
    public static void main(String[] args) {
        Integer[] a = { 5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1 };
        node root = buildTree(a);
        int target = 22;
        System.out.println(hasPathSum(root, target));
        System.out.println(findPaths(root, target));        
        System.out.println(findPathsRecursive(root, target));        

    }
}
