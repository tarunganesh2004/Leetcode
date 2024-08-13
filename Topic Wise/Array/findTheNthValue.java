// LC Find the nth value after K Seconds - 3179
import java.util.*;
public class findTheNthValue {
    public static void main(String[] args) {
        int n = 4;
        int k = 5;
        System.out.println(valueAfterKSeconds(n, k));
    }

    private static int mod = 1000000007;

    public static int valueAfterKSeconds(int n, int k) {
        int[] r = new int[n];
        Arrays.fill(r, 1);
        while (k > 0) {
            for (int i = 1; i < n; i++) {
                r[i] = (r[i] + r[i - 1]) % mod;
            }
            k--;
        }
        return r[n - 1];
    }
}
