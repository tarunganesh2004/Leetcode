import java.util.Arrays;

public class differencebetweenOnesandZeroes {
    public static void main(String[] args) {
        int[][] grid = { { 0, 1, 1 }, { 1,0,1 }, { 0, 0, 1 } };
        System.out.println(Arrays.deepToString(onesMinusZeroes(grid)));
    }

    public static int[][] onesMinusZeroes(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int[][] res = new int[r][c];
        int[] onesRow = new int[r];
        int[] zeroesRow = new int[r];
        int[] onesCol = new int[c];
        int[] zeroesCol = new int[c];

        int oneCount = 0;
        int zeroCount = 0;

        // Calculate counts of ones and zeroes for each row
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 0) {
                    zeroCount++;
                } else {
                    oneCount++;
                }
            }
            onesRow[i] = oneCount;
            zeroesRow[i] = zeroCount;
            oneCount = 0;
            zeroCount = 0;
        }

        // Calculate counts of ones and zeroes for each column
        for (int j = 0; j < c; j++) {
            for (int i = 0; i < r; i++) {
                if (grid[i][j] == 0) {
                    zeroCount++;
                } else {
                    oneCount++;
                }
            }
            onesCol[j] = oneCount;
            zeroesCol[j] = zeroCount;
            oneCount = 0;
            zeroCount = 0;
        }

        // Calculate the differences according to the provided formula
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                res[i][j] = onesRow[i] - zeroesRow[i] + onesCol[j] - zeroesCol[j];
            }
        }
        return res;
    }
}
