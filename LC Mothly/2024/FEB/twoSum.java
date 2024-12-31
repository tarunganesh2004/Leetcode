import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class twoSum {
    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        System.out.println(Arrays.toString(twosum(nums, target)));
    }

    public static int[] twosum(int[] nums,int target){
        Map<Integer, Integer> mp = new HashMap<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (mp.containsKey(complement)) {
                return new int[] { mp.get(complement), i };
            }
            mp.put(nums[i], i);
        }
        return new int[] {};
    }
}
