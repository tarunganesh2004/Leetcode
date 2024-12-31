import java.util.Arrays;

class perfectSquares {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return solve(n, dp);
    }

    private int solve(int n, int[] dp) {
        if (n == 0) return 0;

        if (dp[n] != -1) {
            return dp[n];
        }

        int ans = n;
        for (int i = 1; i * i <= n; i++) {
            ans = Math.min(ans, solve(n - i * i, dp) + 1);
        }

        dp[n] = ans;
        return ans;
    }

    public static void main(String[] args) {
        perfectSquares solution = new perfectSquares();
        int n = 12;
        System.out.println("Minimum number of perfect squares to sum up to " + n + ": " + solution.numSquares(n));
    }
}
