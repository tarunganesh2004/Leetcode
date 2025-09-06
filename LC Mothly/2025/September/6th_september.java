// Minimum Operations to Make Array Elements Zero LC 3495(Hard)

// import java.util.*;

class Solution {
    public static void main(String[] args) {
        int[][] queries={{1,2},{2,4}};
        System.out.println(minimumOperations(queries));
    }

    public static long get(int n) {
        long c = 0;
        int i = 1;
        int base = 1;
        while (base <= n) {
            int end = Math.min(base * 2 - 1, n);
            c += (long) ((i + 1) / 2) * (end - base + 1);
            i++;
            base *= 2;

        }
        return c;
    }

    public static long minimumOperations(int[][] queries) {
        long res = 0;
        for (int[] q : queries) {
            long c1 = get(q[1]);
            long c2 = get(q[0] - 1);
            res += (c1 - c2 + 1) / 2;
        }
        return res;
    }
}