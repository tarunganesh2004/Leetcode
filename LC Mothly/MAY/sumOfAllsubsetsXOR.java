// leetcode 1863
// [1,3 ] --> subsets [1],[3],[1,3],, [1] has XOR 1, [3] has XOR 3,[1,3] has XOR  1^3==2 , so sum=1+3+2=6


import java.util.*;
class sumOfAllSubsetsXOR {
    public static void main(String[] args) {
        int[] a = { 1, 3 };
        int s = XORSUM(a);
        System.out.println(s);
    }

    public static int XORSUM(int[] a) {
        List<List<Integer>> allsubsets = findSubsets(a);
        int res = 0;
        for (List<Integer> s : allsubsets) {
            int subsetXOR = 0;
            for (int nums : s) {
                subsetXOR ^= nums;
            }
            res += subsetXOR;
        }

        return res;
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