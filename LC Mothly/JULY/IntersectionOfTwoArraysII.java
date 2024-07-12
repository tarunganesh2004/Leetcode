import java.util.*;

public class IntersectionOfTwoArraysII {
    public static void main(String[] args) {
        int[] a1 = { 1, 2, 2, 1 };
        int[] a2 = { 2, 2 };
        System.out.println(Arrays.toString(intersect(a1, a2)));
    }

    public static int[] intersect(int[] a1, int[] a2) {
        Arrays.sort(a1);
        Arrays.sort(a2);
        List<Integer> l = new ArrayList<>();
        int i = 0;
        int j = 0;
        while (i < a1.length && j < a2.length) {
            if (a1[i] == a2[j]) {
                l.add(a1[i]);
                i++;
                j++;
            } else if (a1[i] < a2[j]) {
                i++;
            } else {
                j++;
            }
        }
        int[] res = new int[l.size()];
        for (int k = 0; k < l.size(); k++) {
            res[k] = l.get(k);
        }
        return res;
    }
}
