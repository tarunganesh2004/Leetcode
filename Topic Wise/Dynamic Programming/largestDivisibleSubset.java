// LC 368
// Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
// answer[i] % answer[j] == 0, or
// answer[j] % answer[i] == 0
// If there are multiple solutions, return any of them.
import java.util.*;
public class largestDivisibleSubset {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3 };
        System.out.println(largestDivisible(a));

    }

    public static List<Integer> largestDivisible(int[] a) {
        Arrays.sort(a);
        int n = a.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int[] prev = new int[n];
        Arrays.fill(prev, -1);

        int maxSize = 1;
        int maxIndex = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (a[i] % a[j] == 0 && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }

            }
            if (dp[i] > maxSize) {
                maxSize = dp[i];
                maxIndex = i;
            }
        }
        List<Integer> res = new ArrayList<>();
        while (maxIndex != -1) {
            res.add(a[maxIndex]);
            maxIndex = prev[maxIndex];
        }
        Collections.reverse(res);
        return res;
    }
}
