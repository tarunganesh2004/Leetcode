import java.util.*;
class concatenate {
    public static void main(String[] args) {
        String[] s = { "abc", "ab", "b" };
        System.out.println(largestLexicographical(s));
    }

    static String largestLexicographical(String[] s) {
        Arrays.sort(s, (x, y) -> (y + x).compareTo(x + y));
        StringBuilder sb = new StringBuilder();
        for (String i : s) {
            sb.append(i);
        }
        return sb.toString();
    }
}
