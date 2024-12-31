// longest Nice Subarray -- Leetcode 2401
public class longestNiceSubarray {
    public static void main(String[] args) {
        int[] a = { 1, 3, 8, 48, 10 };
        System.out.println(longestnicesubarray(a));
    }

    public static int longestnicesubarray(int[] nums) {
        int j = 0;
        int num = 0; // contains setbits of all arrays
        int ans = 0; // to store result
        for (int i = 0; i < nums.length; i++) {
            while ((num & nums[i]) != 0) {
                // keep removing numbers from backside unless the problem is solved
                num = num ^ nums[j]; // unset the bits by nums[j] (1^1=0)
                j++;
            }
            // if equal to zero
            num = num | nums[i];
            ans = Math.max(ans, i - j + 1); // i-j+1 is length of longest nice subarray
        }
        return ans;
    }
}
