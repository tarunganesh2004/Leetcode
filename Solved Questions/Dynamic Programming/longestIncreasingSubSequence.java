import java.util.Arrays;

class longestIncreasingSubSequence {
    public static void main(String[] args) {
        int[] a = { 10, 9, 2, 5, 3, 7, 101, 18 };
        System.out.println(longest(a));
    }

    public static int longest(int[] a) {
        int n = a.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int maxLen = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (a[j] < a[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }
        System.out.println(Arrays.toString(dp));
        return maxLen;
    }
}