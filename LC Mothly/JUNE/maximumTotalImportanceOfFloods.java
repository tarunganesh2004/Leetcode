// LC 2285

import java.util.Arrays;

public class maximumTotalImportanceOfFloods {
    public static void main(String[] args) {
        int[][] roads = { { 0, 1 }, { 1, 2 }, { 2, 3 }, { 0, 2 }, { 1, 3 }, { 2, 4 } };
        int n = 5;
        int[] d = new int[n];
        for (int[] r : roads) {
            d[r[0]]++;
            d[r[1]]++;
            // System.out.println(Arrays.toString(d));
        }
        Arrays.sort(d);
        // System.out.println(Arrays.toString(d));
        int totalImportance = 0;
        int value = 1;
        for (int r : d) {
            totalImportance += r * value;
            value++;
        }
        System.out.println(totalImportance);
    }
}
