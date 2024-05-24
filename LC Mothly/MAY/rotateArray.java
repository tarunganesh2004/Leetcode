import java.util.Arrays;

public class rotateArray {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5 };
        int k = 2;
        // System.out.println(Arrays.toString(rotateLeft(a)));
        // System.out.println(Arrays.toString(rotateByK(a, k)));
        // System.out.println(Arrays.toString(rotateByKAnother(a, k)));
        System.out.println(Arrays.toString(rotateToLeft(a, k)));
        System.out.println(Arrays.toString(rotateToRightByK(a, k)));
    }

    // Using Extra memory
    public static int[] rotateLeft(int[] a) {
        int n = a.length;
        int[] r = new int[n];
        for (int i = 1; i < n; i++) {
            r[i - 1] = a[i];
        }
        r[n - 1] = a[0];
        return r;

    }

    public static int[] rotateLeft1(int[] a) {
        // using O(1) memory
        int n = a.length;
        int temp = a[0];
        for (int i = 0; i < n - 1; i++) {
            a[i] = a[i + 1];
        }
        a[n - 1] = temp;
        return a;
    }

    public static int[] rotateByK(int[] a, int k) {
        int n = a.length;
        int[] r = new int[n];
        k = k % n; // for cases where k>=n
        for (int i = 0; i < n; i++) {
            r[i] = a[(i + k) % n];
        }
        return r;
    }

    public static int[] rotateByKAnother(int[] a, int k) {
        int n = a.length;
        k = k % n;
        int[] temp = new int[k];
        for (int i = 0; i < k; i++) {
            temp[i] = a[i]; // copying the 1st k elements into the temp array
        }
        // Shift n-k elements from last by k position to the left
        for (int i = 0; i < n - k; i++) {
            a[i] = a[i + k];
        }
        // Copy the elements into the main array from the temp array
        for (int i = n - k; i < n; i++) {
            a[i] = temp[i - n + k];
        }
        return a;
    }

    // Optimal Approach
    // By using reversal Approach
    public static int[] rotateToLeft(int[] a, int k) {
        int n = a.length;
        reverse(a, 0, k - 1); // reverse 1st k elements
        reverse(a, k, n - 1); // reverse last n-k elements
        reverse(a, 0, n - 1); // reverse whole array
        return a;
    }

    public static void reverse(int[] a, int start, int end) {
        while (start < end) {
            int temp = a[start];
            a[start] = a[end];
            a[end] = temp;
            start++;
            end--;
        }
    }

    // Rotate k steps right
    public static int[] rotateToRightByK(int[] a, int k) {
        int n = a.length;
        // reverse 1st n-k elements
        reverse(a, 0, n - k - 1);
        // reverse last k elements
        reverse(a, n - k, n - 1);
        // reverse whole array
        reverse(a, 0, n - 1);
        return a;
    }
}
