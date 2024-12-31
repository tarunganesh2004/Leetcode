// Longest Arithmetic Sequence of given difference

import java.util.HashMap;
import java.util.Map;

public class longestArithmeticSequence {
    public static void main(String[] args) {
        int[] a = { 1, 5, 7, 8, 5, 3, 4, 2, 1 };
        int diff = -2;
        System.out.println(longestSubsequence(a, diff));
    }

    public static int longestSubsequence(int[] arr, int difference) {
        int n = arr.length;
        int[] dp = new int[n];
        Map<Integer, Integer> map = new HashMap<>();
        int max = 1;
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            if (map.containsKey(arr[i] - difference)) {
                dp[i] = dp[map.get(arr[i] - difference)] + 1;
            }
            map.put(arr[i], i);
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
