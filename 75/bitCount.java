import java.util.Arrays;

public class bitCount {
    public static void main(String[] args) {
        int n = 5;
        System.out.println(Arrays.toString(countbits(n)));
    }

    public static int[] countbits(int n) {
        int[] a = new int[n+1];
        for (int i = 0; i < n+1;i++){
            int c1 = Integer.bitCount(i);
            a[i] = c1;
        }
        return a;
    }
}
