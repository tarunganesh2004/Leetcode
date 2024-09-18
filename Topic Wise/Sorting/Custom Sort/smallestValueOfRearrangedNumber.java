import java.util.*;
public class smallestValueOfRearrangedNumber {
    public static void main(String[] args) {
        int n = 310;
        System.out.println(smallest(n));
    }

    static long smallest(int n) {
        String s = String.valueOf(Math.abs(n));
        char[] d = s.toCharArray();
        if (n > 0) { // positive number
            Arrays.sort(d);
            if (d[0] == '0') {
                // find the first non-zero digit
                for (int i = 1; i < d.length; i++) {
                    if (d[i] != 0) {
                        char temp = d[0];
                        d[0] = d[i];
                        d[i] = temp;
                        break;
                    }
                }
            }
            String r = new String(d);
            return Long.parseLong(r);
        } else {
            // negative number , so sort in descending order
            Character[] d1 = new Character[d.length];
            for (int i = 0; i < d.length; i++) {
                d1[i] = d[i];
            }
            Arrays.sort(d1, (a, b) -> Character.compare(b, a));
            StringBuilder sb = new StringBuilder();
            for (Character i : d1) {
                sb.append(i);
            }
            return -Long.parseLong(sb.toString());
        }
        
    }
}
