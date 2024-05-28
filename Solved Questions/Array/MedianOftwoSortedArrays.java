import java.util.Arrays;

public class MedianOftwoSortedArrays {
    public static void main(String[] args) {
        int[] a1 = { 1, 3 };
        int[] a2 = { 2 };
        int[] a3 = new int[a1.length + a2.length];
        System.arraycopy(a1, 0, a3, 0, a1.length);
        System.arraycopy(a2, 0, a3, a1.length, a2.length);

        System.out.println("Concatenated Array: " + Arrays.toString(a3));

        Arrays.sort(a3);

        double ans;
        if (a3.length % 2 == 0) {
            int n1 = a3[a3.length / 2];
            int n2 = a3[(a3.length / 2) - 1];
            ans = (n1 + n2) / 2.0;
        } else {
            ans = a3[a3.length / 2];
        }

        System.out.println("Median: " + ans);

        // Time complexity O((n1+n2)log(n1+n2))
    }

    // Optimized Approach Using Binary Search O(log(m+n))
}
