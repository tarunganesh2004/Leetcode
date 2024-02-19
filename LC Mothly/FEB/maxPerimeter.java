// Polygon with maximum perimeter
// feb-15


import java.util.Arrays;

public class maxPerimeter {
    public static void main(String[] args) {
        int[] a = { 1, 12, 1, 2, 5, 50, 3 };
        long r = getPerimeter(a);
        System.out.println(r);
    }

    public static long getPerimeter(int[] nums) {
        Arrays.sort(nums);
        long perimeter = 0;
        long ans = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < perimeter) {
                ans = nums[i] + perimeter;
            }
            perimeter += nums[i];
        }
        return ans;
    }
}
