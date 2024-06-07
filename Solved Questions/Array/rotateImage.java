import java.util.Arrays;

class rotateImage{
    public static void main(String[] args) {
        int[][] a = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        // o/p : 
        // 7 4 1
        // 8 5 2
        // 9 6 3
        System.out.println(Arrays.deepToString(rotate1(a)));
        // System.out.println(Arrays.deepToString(rotate2(a)));
    }

    public static int[][] rotate1(int[][] a) {
        int r = a.length;
        // using extra space
        // Space Complexity O(n^2)
        int[][] ans = new int[r][r];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < r; j++) {
                ans[j][r - 1 - i] = a[i][j];
            }
        }
        return ans;
    }
    // without using extra space
    public static int[][] rotate2(int[][] a) {
        // int r = a.length;
        // Transpose of the matrix and then reverse each row
        for (int i = 0; i < a.length; i++) {
            for (int j = i; j < a[0].length; j++) {
                // Transpose
                int temp = a[i][j];
                a[i][j] = a[j][i];
                a[j][i] = temp;
            }
        }
        for (int i = 0; i < a.length; i++) {
            reverse(a[i]);
        }

        return a;
    }

    public static void reverse(int[] a) {
        int s = 0;
        int e = a.length - 1;
        while (s < e) {
            int temp = a[s];
            a[s] = a[e];
            a[e] = temp;
            s++;
            e--;
        }
    }
}