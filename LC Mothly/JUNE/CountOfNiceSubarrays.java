// LC 1248 Count Number of Nice Subarrays
import java.util.*;

public class CountOfNiceSubarrays {
    public static void main(String[] args) {
        int[] nums = { 1, 1, 2, 1, 1 };
        int k = 3;
        System.out.println(countofnicesubarrays(nums, k));
        System.out.println(countnice(nums, k));
    }


    // O(n^3) Bruteforce
    public static int countofnicesubarrays(int[] a, int k) {
        List<int[]> l = new ArrayList<>();
        int n = a.length;
        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                int[] s = Arrays.copyOfRange(a, start, end + 1);
                l.add(s);
            }
        }
        int c = 0;
        for (int[] r : l) {
            int t = countOdd(r);
            if(t==k){
                c++;
            }
        }
        return c;
    }

    public static int countOdd(int[] a) {
        int c = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] % 2 != 0) {
                c++;
            }
        }
        return c;
    }
    
    // Optimized O(n)
    public static int countnice(int[] a, int k) {
        // using prefix sums
        int[] prefixCount = new int[a.length + 1];
        int c = 0;
        prefixCount[0] = 1;
        int oddCount = 0;
        for (int num : a) {
            if (num % 2 != 0) {
                oddCount++;
            }
            if (oddCount >= k) {
                c += prefixCount[oddCount - k];
            }
            prefixCount[oddCount]++;
        }
        return c;
    }
}
