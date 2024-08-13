// LC 673
import java.util.Arrays;

public class NumberOfLongestIncreasingSubSequences {
    public static void main(String[] args) {
        int[] a = { 1, 3, 5, 4, 7 };
        System.out.println(numberOfLongest(a)); // Expected output: 2
    }

    public static int numberOfLongest(int[] a) {
        if (a.length == 0) {
            return 0;
        }

        int n = a.length;
        int[] dp = new int[n];
        int[] count = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(count, 1);

        int maxLen = 0;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) { 
                if (a[j] < a[i]) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        count[i] = count[j];
                    } else if (dp[j] + 1 == dp[i]) {
                        count[i] += count[j];
                    }
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == maxLen) {
                res += count[i];
            }
        }

        return res;
    }
}
