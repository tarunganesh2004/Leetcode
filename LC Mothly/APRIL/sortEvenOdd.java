import java.util.Arrays;

public class sortEvenOdd {
    public static void main(String[] args) {
        int[] a = { 36, 45, 32, 31, 15, 41, 9, 46, 36, 6, 15, 16, 33, 26, 27, 31, 44, 34};
        int n = a.length;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 1) {
                if (i + 2 <= n - 1) {
                    int temp = a[i];
                    a[i] = a[i + 2];
                    a[i + 2] = temp;
                }
            }
        }
            for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                if (i + 2 <= n - 1) {
                    int temp = a[i];
                    a[i] = a[i + 2];
                    a[i + 2] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(a));
    }
}
