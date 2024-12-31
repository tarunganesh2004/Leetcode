import java.util.Arrays;

public class rotateArray {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5 };
        int k = 3;
        rotate(a, k);
    }

    public static void rotate(int[] a, int k) {
        k = k % a.length;
        int n = a.length;
        reverseNum(a, 0, n - 1);
        reverseNum(a, 0, k - 1);
        reverseNum(a, k, n - 1);
        System.out.println(Arrays.toString(a));

    }

    public static void reverseNum(int[] a, int start, int end) {
        while (start < end) {
            int temp = a[start];
            a[start] = a[end];
            a[end] = temp;
            start++;
            end--;
        }
    }
}
