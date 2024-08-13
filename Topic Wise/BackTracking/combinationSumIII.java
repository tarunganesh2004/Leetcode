// LC 216
import java.util.*;
public class combinationSumIII {
    public static void main(String[] args) {
        int k = 3;
        int n = 9;
        System.out.println(combinationsum3(k, n));
    }

    public static List<List<Integer>> combinationsum3(int k, int n) {
        List<List<Integer>> l = new ArrayList<>();
        List<Integer> temp = new ArrayList<>();
        backtrack(l, temp, k, n, 1);
        return l;
    }

    private static void backtrack(List<List<Integer>> l, List<Integer> tmpList, int k, int remain, int start) {
        if (remain < 0 || tmpList.size() > k)
            return;
        if (remain == 0 && tmpList.size() == k) {
            l.add(new ArrayList<>(tmpList));
        }
        else {
            for (int i = start; i <= 9; i++) {
                tmpList.add(i);
                backtrack(l, tmpList, k, remain - i, i + 1);
                tmpList.remove(tmpList.size() - 1);
            }
        }
    }
}
