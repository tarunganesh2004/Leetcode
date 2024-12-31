// Feb-14
// Rearrange array elements by Sign
// i/p : [1,2,3,-1,-2,-3] , o/p : [1,-1,2,-2,3,-3]

import java.util.Arrays;

public class rearrangeArray {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, -1, -2, -3 };
        int[] r = rearrangearray(a);
        System.out.println(Arrays.toString(r));
    }

    public  static int[] rearrangearray(int[] nums) {
        int n = nums.length;
        int[] a = new int[n];
        int pos = 0;// for positive numbers
        int neg = 1;// for negative numbers
        for (int i = 0; i < n; i++) {
            if (nums[i] >= 0) {
                a[pos] = nums[i];
                pos += 2;
            } else {
                a[neg] = nums[i];
                neg += 2;
            }
        }
        return a;
    }
}
