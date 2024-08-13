// LC 39
import java.util.*;
public class combinationSum {
    public static void main(String[] args) {
        int[] candidates = { 2, 3, 5 };
        int target = 8;
        System.out.println(combinationsum(candidates, target));
    }

    public static List<List<Integer>> combinationsum(int[] nums, int target) {
        List<List<Integer>> l = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
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
                tmpList.add(nums[i]);
                backtrack(l, tmpList, nums, remain - nums[i], i);
                tmpList.remove(tmpList.size() - 1);
            }
        }
    }
}
