import java.util.ArrayList;
import java.util.List;
public class countSubsets {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3 };
        int[] b = { 4,6,1,2 };
        List<List<Integer>> subsets = findSubsets(b);
        List<List<Integer>> subsets1 = subsets(a);
        System.out.println(subsets);
        System.out.println(subsets1);
    }

    public static List<List<Integer>> findSubsets(int[] a) {
        List<List<Integer>> allsubsets= new ArrayList<>();
        backtrack(allsubsets, new ArrayList<>(), a, 0);
        return allsubsets;
    }

    public static void backtrack(List<List<Integer>> allsubsets, List<Integer> subset, int[] a, int start) {
        allsubsets.add(new ArrayList<>(subset));
        for (int i = start; i < a.length; i++) {
            subset.add(a[i]);
            backtrack(allsubsets, subset, a, i+ 1);
            subset.remove(subset.size() - 1);
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
