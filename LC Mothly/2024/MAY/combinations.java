// LC 77. Combinations
import java.util.*;
public class combinations {
    public static void main(String[] args) {
        int n = 4;
        int k = 2;
        List<List<Integer>> res = combine(n, k);
        System.out.println(res);
    }

    public static List<List<Integer>> combine(int n, int k) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = i + 1;
        }
        List<List<Integer>> res = generateSubsets(a, k);
        return res;
    }

    public static List<List<Integer>> generateSubsets(int[] a, int k) {
        List<List<Integer>> l = new ArrayList<>();
        backtrack(l, new ArrayList<>(), 0, a, k);
        return l;
    }

    public static void backtrack(List<List<Integer>> l, List<Integer> subset, int start, int[] a, int k) {
        if (subset.size() == k) {
            l.add(new ArrayList<>(subset));
            return;
        }
        for (int i = start; i < a.length; i++) {
            subset.add(a[i]);
            backtrack(l, subset, i + 1, a, k);
            subset.remove(subset.size() - 1);
        }
    }
}
