import java.util.Arrays;

class absoluteDifferencesinSortedArray {
    public static void main(String[] args) {
        int[] nums = { 2, 3, 5 };
        System.out.println(Arrays.toString(getSumAbsoluteDifferences(nums)));
        System.out.println(Arrays.toString(getAbsoluteDifferences(nums)));
    }

    public static int[] getSumAbsoluteDifferences(int[] nums) {
        int[] res = new int[nums.length];
        int n = nums.length;
        for (int i = 0; i < nums.length; i++) {
            int j = 0;
            while (j < n) {
                res[i] += Math.abs(nums[i] - nums[j]);
                j++;
                if (j >= n) {
                    break;
                }
            }
        }
        return res; // passes for all small test cases(doesnt work for long test cases)
    }

    public static int[] getAbsoluteDifferences(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = sum - (n - 2 * i) * nums[i];
            sum = sum - 2 * nums[i];
        }
        return res;
    }
}