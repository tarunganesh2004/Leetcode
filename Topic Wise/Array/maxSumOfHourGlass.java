public class maxSumOfHourGlass {
    public static void main(String[] args) {
        int[][] a = { { 1, 2, 3, 0, 0 },
                { 0, 0, 0, 0, 0 },
                { 2, 1, 4, 0, 0 },
                { 0, 0, 0, 0, 0 },
                { 1, 1, 0, 1, 0 } };
        System.out.println(maxSumHour(a));
    }

    public static int maxSumHour(int[][] a) {
        int r = a.length;
        int c = a[0].length;
        if (r < 3 || c < 3) // if less than 3 not possible
            return -1;
        
        int sum = Integer.MIN_VALUE;
        for (int i = 0; i < r - 2; i++) {
            for (int j = 0; j < c - 2; j++) {
                int temp = (a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1]
                        + a[i + 2][j + 2]);
                sum = Math.max(sum, temp);
            }
        }
        return sum;

    }
}
