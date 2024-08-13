// LC 131
import java.util.*;
public class palindromicPartioning {
    public static void main(String[] args) {
        String s = "aab";
        System.out.println(palindromicpartioning(s));
    }

    public static List<List<String>> palindromicpartioning(String s) {
        List<List<String>> l = new ArrayList<>();
        List<String> temp = new ArrayList<>();
        backtrack(l, temp, s, 0);
        return l;
    }

    private static void backtrack(List<List<String>> l, List<String> tmpList, String s, int start) {
        if (start == s.length()) {
            l.add(new ArrayList<>(tmpList));
        } else {
            for (int i = start; i < s.length(); i++) {
                if (isPalindrome(s, start, i)) {
                    tmpList.add(s.substring(start, i + 1));
                    backtrack(l, tmpList, s, i + 1);
                    tmpList.remove(tmpList.size() - 1);
                }
            }
        }
    }
    
    private static boolean isPalindrome(String s, int low, int high) {
        while (low < high) {
            if (s.charAt(low++) != s.charAt(high--))
                return false;
        }
        return true;
    }
}
