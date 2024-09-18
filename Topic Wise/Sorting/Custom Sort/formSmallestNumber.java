import java.util.*;
public class formSmallestNumber {
    public static void main(String[] args) {
        int[] a = { 3, 30, 34, 5, 9 };
        System.out.println(smallest(a));
    }

    static String smallest(int[] a){
        String[] s=new String[a.length];
        for (int i = 0; i < a.length; i++) {
            s[i] = String.valueOf(a[i]);
        }
        System.out.println(Arrays.toString(s));
        Arrays.sort(s, (x, y) -> (x + y).compareTo(y + x));
        System.out.println(Arrays.toString(s));
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
