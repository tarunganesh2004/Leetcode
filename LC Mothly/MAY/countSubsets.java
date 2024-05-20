import java.util.ArrayList;
import java.util.List;
public class countSubsets {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3 };
        List<List<Integer>> subsets = findSubsets(a);
        System.out.println(subsets);
    }

    public static List<List<Integer>> findSubsets(int[] a) {
        List<List<Integer>> allsubsets = new ArrayList<>();
        backtrack(0, a, new ArrayList<>(), allsubsets);
        return allsubsets;
    }

    private static void backtrack(int start, int[] a, List<Integer> currentSubset, List<List<Integer>> allsubsets) {
        allsubsets.add(new ArrayList<>(currentSubset));

        for (int i = start; i < a.length; i++) {
            currentSubset.add(a[i]);
            backtrack(i + 1, a, currentSubset, allsubsets);
            currentSubset.remove(currentSubset.size() - 1);
        }
    }

    // Using Bit Manipulation
    public static List<List<Integer>> subsets(int[] a) {
        List<List<Integer>> res = new ArrayList<>();
        int n = a.length;
        int subsetcount = 1 << n; //2^n
        for (int mask = 0; mask < subsetcount; mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    subset.add(a[i]);
                }
            }
            res.add(subset);
        }
        return res;
    }
}
