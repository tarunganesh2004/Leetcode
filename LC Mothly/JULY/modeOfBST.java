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

public class modeOfBST {
    public static node insert(node root, int n) {
        if (root == null) {
            return new node(n);
        } else if (root.data < n) {
            root.right = insert(root.right, n);
        } else {
            root.left = insert(root.left, n);
        }
        return root;
    }

    public static node create(Integer[] a) {
        node root = null;
        for (Integer n : a) {
            if (n != null) {
                root = insert(root, n);
            }
        }
        return root;
    }

    public static void inorder(node root, Map<Integer, Integer> count) {
        if (root == null)
            return;
        inorder(root.left, count);
        // l.add(root.data);
        count.put(root.data, count.getOrDefault(root.data, 0) + 1);
        inorder(root.right, count);
    }

    public static int[] findMode(node root) {
        Map<Integer, Integer> countMap = new HashMap<>();
        inorder(root, countMap);
        int maxCount = 0;
        for (int c : countMap.values()) {
            if (c > maxCount) {
                maxCount = c;
            }
        }
        List<Integer> res = new ArrayList<>();
        for (int key : countMap.keySet()) {
            if (countMap.get(key) == maxCount) {
                res.add(key);
            }
        }
        int[] r = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            r[i] = res.get(i);
        }
        return r;
    }
    
    public static void main(String[] args) {
        Integer[] a = { 1, null, 2, 2 };
        node root = create(a);
        int[] res = findMode(root);
        System.out.println(Arrays.toString(res));
        
    }
}
