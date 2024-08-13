// LC 40
import java.util.*;
public class combinationSumII {
    public static void main(String[] args) {
        int[] candidates = { 10, 1, 2, 7, 6, 1, 5 };
        int target = 8;
        System.out.println(combinationsum2(candidates, target));
    }

    public static List<List<Integer>> combinationsum2(int[] nums, int target) {
        List<List<Integer>> l = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(l, temp, nums, target, 0);
        return l;
    }

    private static void backtrack(List<List<Integer>> l, List<Integer> tmpList, int[] nums, int remain, int start) {
        if (remain < 0)
            return;
        if (remain == 0) {
            l.add(new ArrayList<>(tmpList));
        }
        else {
            for (int i = start; i < nums.length; i++) {
                if (i > start && nums[i] == nums[i - 1])
                    continue;
                
                tmpList.add(nums[i]);
                backtrack(l, tmpList, nums, remain - nums[i], i + 1);
                tmpList.remove(tmpList.size() - 1);
            }
        }
    }
}
