import java.util.ArrayList;
import java.util.List;

public class palindromicPartioning {
    public static void main(String[] args) {
        String s = "aab";
        // List<List<String>> l = generate(s);
        System.out.println(partition(s));
    }
    
    public static List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), s, 0);
        return res;
    }

    public static void backtrack(List<List<String>> res, List<String> tempList, String s, int start) {
        if (start == s.length()) {
            res.add(new ArrayList<>(tempList));
        } else {
            for (int i = start; i < s.length(); i++) {
                if (isPalindrome(s, start, i)) {
                    tempList.add(s.substring(start, i + 1));
                    backtrack(res, tempList, s, i + 1);
                    tempList.remove(tempList.size() - 1);
                }
            }
        }
        
    }

    public static boolean isPalindrome(String s, int low, int high) {
        while (low < high) {
            if (s.charAt(low++) != s.charAt(high--)) {
                return false;
            }
        }
        return true;
    }

    // public static List<List<String>> generate(String s) {
    //     List<List<String>> allsubsets = new ArrayList<>();
    //     backtrack(allsubsets, new ArrayList<>(), s, 0);
    //     return allsubsets;
    // }

    // public static void backtrack(List<List<String>> allsubsets, List<String> subset, String s, int start) {
    //     // allsubsets.add(new ArrayList<>(subset));
    //     for (int i = start; i < s.length(); i++) {
    //         for (int j = i + 1; j <= s.length(); j++) {
    //             String s1 = s.substring(i, j);
    //             subset.add(s1);
    //             allsubsets.add(new ArrayList<>(subset));
    //             backtrack(allsubsets, subset, s, i + 1);
    //             subset.remove(subset.size() - 1);
    //         }
    //         // String s1 = s.charAt(i) + "";
            
    //     }
    // }
    
    
}
