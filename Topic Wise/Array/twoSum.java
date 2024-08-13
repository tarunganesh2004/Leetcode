import java.util.*;

public class twoSum {
    public static void main(String[] args) {
        int[] a = { 2, 7, 11, 15 };
        int t = 9;
        int[] res = twosumanother(a, t);
        System.out.println(Arrays.toString(res));
    }

    public static int[] twosum(int[] a, int t) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < a.length; i++) {
            int d = t - a[i];
            if (m.containsKey(d)) {
                return new int[] { m.get(d), i };
            }
            m.put(a[i], i);
        }
        return new int[] { -1, -1 };
    }
    // another way
    public static int[] twosumanother(int[] a, int t) {
        for (int i = 1; i < a.length; i++) {
            for (int j = i; j < a.length; j++) {
                if (a[j] + a[j - i] == t) {
                    return new int[] { j-i,j };
                }
            }
        }
        return null;
    }
}
