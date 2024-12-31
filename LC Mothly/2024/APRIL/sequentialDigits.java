import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class sequentialDigits {
    public static void main(String[] args) {
        int low = 10;
        int high = 1000000000;
        List<Integer> res = sequential(low, high);
        System.out.println(res);
    }

    // Brute force Approach takes More time
    // public static List<Integer> sequential(int low, long high) {
    //     List<Integer> ans = new ArrayList<>();
    //     for (int i = low; i <= high; i++) {
    //         if (isSequential(i)) {
    //             ans.add(i);
    //         }
    //     }
    //     return ans;
    // }

    // public static boolean isSequential(int n) {
    //     String numberString = String.valueOf(n);
    //     int len = numberString.length();
    //     // int[] digits = new int[len];
    //     for (int i = 0; i < len - 1; i++) {
    //         if (numberString.charAt(i + 1) - numberString.charAt(i) != 1) {
    //             return false;
    //         }
    //     }
    //     return true;
    // }
    public static List<Integer> sequential(int low, int high) {
        int[] possible = { 12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567,
                5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678,
                3456789, 12345678, 23456789, 123456789 };
        int n = possible.length;
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (low <= possible[i] && high >= possible[i]) {
                ans.add(possible[i]);
            }
        }
        return ans;
}
}
