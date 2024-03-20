// import java.util.Arrays;

public class maximumSwap {
    public static void main(String[] args) {
        int n = 9273;
        System.out.println(maxSwap(n));
        // char[] digits = Integer.toString(n).toCharArray();
        // System.out.println(Arrays.toString(digits));
        // int[] last = new int[10];
        // for (int i = 0; i < digits.length; i++) {
        //     last[digits[i] - '0'] = i;
        //     System.out.println(last[i]);
        // }
    }

    public static int maxSwap(int n) {
        char[] digits = Integer.toString(n).toCharArray();

        int[] last = new int[10];
        for (int i = 0; i < digits.length; i++) {
            last[digits[i] - '0'] = i;
        }

        for (int i = 0; i < digits.length; i++) {
            for (int d = 9; d > digits[i] - '0'; d--) {
                if (last[d] > i) {
                    char temp = digits[i];
                    digits[i] = digits[last[d]];
                    digits[last[d]] = temp;
                    return Integer.valueOf(new String(digits));
                }
            }
        }
        return n;
    }
}
