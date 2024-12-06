public class UniqueBinarySearchTrees {

    // Function to calculate the number of unique BSTs using Catalan number approach
    public int numTrees(int n) {
        // dp[i] will store the number of unique BSTs that can be formed with i nodes
        int[] dp = new int[n + 1];

        // Base cases
        dp[0] = 1; // Empty tree is one possibility
        dp[1] = 1; // One node tree is one possibility

        // Build the dp array using the recursive relation
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }

        return dp[n]; // Return the result for n nodes
    }

    public static void main(String[] args) {
        UniqueBinarySearchTrees solution = new UniqueBinarySearchTrees();

        int n = 5; // Example: Number of nodes
        System.out.println("Number of unique BSTs with " + n + " nodes: " + solution.numTrees(n));
    }
}
