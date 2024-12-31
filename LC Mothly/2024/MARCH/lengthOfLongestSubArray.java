// Length of longest subarray with atmost frequency k

import java.util.HashMap;
import java.util.Map;

public class lengthOfLongestSubArray {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 1, 2, 3, 1, 2, 3 };
        int k = 2;
    }

    public static int lengthOfLongestSubArraywithAtMostFrequency(int[] a, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int res = 0;
        int l = 0;
        for (int r = 0; r < a.length; r++) {
            int count;
            if (map.containsKey(a[r])) {
                count = map.get(a[r]) + 1;
            } else {
                count = 1;
            }
            map.put(a[r], count);
            while (map.size() > k) {
                count = map.get(a[l]) - 1;
                map.put(a[l], count);
                l++;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }

    public static int find(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int maxLength = 0;
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        for (int num : map.keySet()) {
            if (map.get(num) <= k) {
                maxLength += map.get(num);
            } else {
                maxLength += k;
            }
        }
        return maxLength;
    }
}
