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
}
