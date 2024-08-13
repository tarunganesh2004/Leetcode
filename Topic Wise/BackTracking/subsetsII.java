// LC 90 
// Given an integer array nums that may contain duplicates, return all possible  subsets
// The solution set must not contain duplicate subsets. Return the solution in any order.
import java.util.*;
public class subsetsII {
    public static void main(String[] args) {
        int[] a = { 1, 2, 2 };
        List<List<Integer>> res = generate(a);
        for (List<Integer> l : res) {
            System.out.println(l);
        }
    }

    public static List<List<Integer>> generate(int[] a) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(a);
        backtrack(res, new ArrayList<>(), a, 0);
        return res;
    }

    public static void backtrack(List<List<Integer>> l, List<Integer> subset, int[] a, int start) {
        l.add(new ArrayList<>(subset));
        for (int i = start; i < a.length; i++) {
            if (i > start && a[i] == a[i - 1])
                continue;
            subset.add(a[i]);
            backtrack(l, subset, a, i + 1);
            subset.remove(subset.size() - 1);
        }
    }
}
