// July 19 2024, LC 1380. Lucky Numbers in a Matrix
import java.util.*;

class LuckyNumbers{
    public static void main(String[] args) {
        int[][] m = { { 3, 7, 8 }, { 9, 11, 13 }, { 15, 16, 17 } };
        List<Integer> l = lucky(m);
        System.out.println(l);
    }

    public static List<Integer>  lucky(int[][] m) {
        int r = m.length;
        int c = m[0].length;

        List<Integer> rowMin = new ArrayList<>();
        List<Integer> colMax = new ArrayList<>();
        for (int i = 0; i < r; i++) {
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < c; j++) {
                min = Math.min(min, m[i][j]);
            }
            rowMin.add(min);
        }
        for (int i = 0; i < c; i++) {
            int max = Integer.MIN_VALUE;
            for (int j = 0; j < r; j++) {
                max = Math.max(max, m[j][i]);
            }
            colMax.add(max);
        }
        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (m[i][j] == rowMin.get(i) && m[i][j] == colMax.get(j)) {
                    res.add(m[i][j]);
                }
            }
        }
        return res;
    }
}