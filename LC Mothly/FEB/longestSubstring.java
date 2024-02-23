// longest substring without repeating characters

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class longestSubstring {
    public static void main(String[] args) {
        String s = "abcabcabc";
        System.out.println(longestsubstring(s));
    }

    public static int longestsubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int left = 0;
        int right = 0;
        int n = s.length();
        int len = 0;
        while (right < n) {
            if (map.containsKey(s.charAt(right))) {
                left = Math.max(map.get(s.charAt(right)) + 1, left);
            }
            map.put(s.charAt(right), right);
            len = Math.max(len, right - left + 1);
            right++;
        }
        return len;
    }

    public static int longestsubstringwithoutrepeating(String s) {
        Set<Character> set = new HashSet<>();
        int max = 0;
        int start = 0;
        int end = 0;

        while (end < s.length()) {
            char c = s.charAt(end);
            if (!set.contains(c)) {
                set.add(c);
                max = Math.max(max, end - start + 1);
                end++;
            } else {
                set.remove(s.charAt(start));
                start++;
            }
        }
        return max;
    }
}
