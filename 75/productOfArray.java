// Product of array except self
// Leetcode : 238

import java.util.Arrays;

public class productOfArray {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4 };
        int[] nums1 = { -1, 1, 0, -3, 3 };
        System.out.println(Arrays.toString(productExceptSelf(nums)));
        System.out.println(Arrays.toString(productExceptSelf(nums1)));
    }

    public static int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int right = 1;
        int left = 1;
        for (int i = 0; i < n; i++) {
            res[i] = 1;
        }

        for (int i = 0; i < n; i++) {
            res[i] = res[i] * left;
            left = left * nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            res[i] = res[i] * right;
            right = right * nums[i];
        }
        return res;
    }
}
