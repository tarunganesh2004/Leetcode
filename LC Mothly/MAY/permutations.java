import java.util.ArrayList;
import java.util.List;

public class permutations {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3 };
        List<List<Integer>> p = generatePermutations(a);
        System.out.println(p);
    }

    public static List<List<Integer>> generatePermutations(int[] a) {
        List<List<Integer>> permutations = new ArrayList<>();
        backtrack(permutations, new ArrayList<>(), a, new boolean[a.length]);
        return permutations;
    }

    private static void backtrack(List<List<Integer>> permutations, List<Integer> current, int[] a, boolean[] used) {
        if (current.size() == a.length) {
            permutations.add(new ArrayList<>(current));
        } else {
            for (int i = 0; i < a.length; i++) {
                if (used[i]) {
                    continue;
                }
                used[i] = true;
                current.add(a[i]);
                backtrack(permutations, current, a, used);
                current.remove(current.size() - 1);
                used[i] = false;
            }
        }
    }
}
