// Node class representing each node in a binary search tree (BST)
class BSTNode {
    int data;
    BSTNode left, right;

    // Constructor to create a node
    public BSTNode(int data) {
        this.data = data;
        this.left = this.right = null;
    }
}

public class BinarySearchTree {
    static BSTNode root;

    // Constructor to create a binary search tree with a root node
    public BinarySearchTree(int rootData) {
        root = new BSTNode(rootData);
    }

    // Insert a new node in the BST (maintaining the BST property)
    public static void insert(int data) {
        root = insertRecursive(root, data);
    }

    // Recursive helper method for insertion
    private static BSTNode insertRecursive(BSTNode node, int data) {
        if (node == null) {
            return new BSTNode(data);
        }
        if (data < node.data) {
            node.left = insertRecursive(node.left, data);
        } else if (data > node.data) {
            node.right = insertRecursive(node.right, data);
        }
        return node;
    }

    // Delete a node in the BST (maintaining the BST property)
    public static void delete(int key) {
        root = deleteRecursive(root, key);
    }

    // Recursive helper method for deletion
    private static BSTNode deleteRecursive(BSTNode node, int key) {
        if (node == null) {
            return null;
        }

        if (key < node.data) {
            node.left = deleteRecursive(node.left, key);
        } else if (key > node.data) {
            node.right = deleteRecursive(node.right, key);
        } else {
            // Node with only one child or no child
            if (node.left == null) {
                return node.right;
            } else if (node.right == null) {
                return node.left;
            }
            // Node with two children: Get the inorder successor (smallest in the right
            // subtree)
            node.data = minValue(node.right);

            // Delete the inorder successor
            node.right = deleteRecursive(node.right, node.data);
        }
        return node;
    }

    // Get the minimum value node in the BST
    private static int minValue(BSTNode node) {
        int minValue = node.data;
        while (node.left != null) {
            minValue = node.left.data;
            node = node.left;
        }
        return minValue;
    }

    // In-order traversal (Left -> Root -> Right)
    public static void inOrder(BSTNode node) {
        if (node == null)
            return;
        inOrder(node.left);
        System.out.print(node.data + " ");
        inOrder(node.right);
    }

    // Main method to demonstrate the BST operations
    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree(50); // Root node with value 50

        // Inserting nodes into the BST
        insert(30);
        insert(20);
        insert(40);
        insert(70);
        insert(60);
        insert(80);

        System.out.println("In-order traversal:");
        inOrder(root);
        System.out.println();

        // Delete node with value 20
        delete(20);
        System.out.println("In-order traversal after deletion:");
        inOrder(root);
    }
}
