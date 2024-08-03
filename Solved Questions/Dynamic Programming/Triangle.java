// LC 120 

import java.util.Arrays;

public class Triangle {
    public static void main(String[] args) {
        int[][] t = { { 2 }, { 3, 4 }, { 6, 5, 7 }, { 4, 1, 8, 3 } };
        System.out.println(minimumTotal(t));
    }

    public static int minimumTotal(int[][] t) {
        int n = t.length;
        int[] dp = new int[n]; // initialize dp array with last row of triangle

        // fill the dp array with last row
        for (int i = 0; i < n; i++) {
            dp[i] = t[n - 1][i];
        }

        // start from second last row and fill the dp array
        for (int r = n - 2; r >= 0; r--) {
            // System.out.println(Arrays.toString(dp));
            for (int c = 0; c <= r; c++) {
                dp[c] = t[r][c] + Math.min(dp[c], dp[c + 1]);
            }
            System.out.println(Arrays.toString(dp));
        }
        return dp[0];
    }
}
