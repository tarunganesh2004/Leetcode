import java.util.*;
public class largestNumber {
    public static void main(String[] args) {
        int[] a = { 3, 30, 34, 5, 9 };
        String[] s = new String[a.length];
        for (int i = 0; i < a.length; i++) {
            s[i] = String.valueOf(a[i]);
        }
        // System.out.println(Arrays.toString(s));
        // System.out.println(Arrays.toString(s));
        
        System.out.println(largest(a));
    }

    static String largest(int[] a) {
        String[] s = new String[a.length];
        for (int i = 0; i < a.length; i++) {
            s[i] = String.valueOf(a[i]);
        }
        Arrays.sort(s,(x,y)->(y+x).compareTo(x+y));
        StringBuilder sb = new StringBuilder();
        for (String i : s) {
            sb.append(i);
        }
        if (sb.charAt(0) == '0') {
            return "0";
        }
        return sb.toString();
    }
}
