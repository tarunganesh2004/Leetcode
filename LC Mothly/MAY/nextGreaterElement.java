// import java.util.ArrayList;
// import java.util.Arrays;
// import java.util.List;
import java.util.*;
public class nextGreaterElement {
    public static void main(String[] args) {
        int[] nums1 = { 4, 1, 2 };
        int[] nums2 = { 1, 3, 4, 2 };
        System.out.println(Arrays.toString(nextGreaterArray(nums1, nums2)));
        int[] a = { 3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9 };
        System.out.println(Arrays.toString(nextGreater(a)));
    }

    public static int[] nextGreater(int[] a) {
        int n = a.length;
        int[] res = new int[n];
        Stack<Integer> s = new Stack<>();
        for (int i = 2 * n - 1; i >= 0; i--) {
            while (s.isEmpty() == false && s.peek() <= a[i % n]) {
                s.pop();
            }
            if (i < n) {
                if (s.isEmpty() == false) {
                    res[i] = s.peek();
                } else {
                    res[i] = -1;
                }
            }
            s.push(a[i % n]);
        }
        return res;
    }
    // O(n*m ) Time Complexity
    public static int[] nextGreaterArray(int[] nums1, int[] nums2) {
        List<Integer> l = new ArrayList<>();
        for (int i = 0; i < nums1.length; i++) {
            int r = getGreater(nums1[i], nums2);
            l.add(r);
        }
        int[] res = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            res[i] = l.get(i);
        }
        return res;
    }

    public static int getGreater(int num, int[] nums2) {
        // Find the index of num in nums2
        int index = -1;
        for (int j = 0; j < nums2.length; j++) {
            if (nums2[j] == num) {
                index = j;
                break;
            }
        }

        // If num is not found, return -1
        if (index == -1) {
            return -1;
        }

        // Find the next greater element in nums2
        for (int j = index + 1; j < nums2.length; j++) {
            if (nums2[j] > num) {
                return nums2[j];
            }
        }

        // If no greater element is found, return -1
        return -1;
    }
}
