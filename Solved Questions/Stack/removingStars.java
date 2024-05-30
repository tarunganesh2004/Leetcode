// lC 2390
import java.util.*;

class removeStars {
    public static void main(String[] args) {
        String s = "leet**cod*e"; // o/p: lecoe
        String s1 = "erase*****";
        System.out.println(remove(s));
        System.out.println(remove(s1));
    }

    public static String remove(String s) {
        Stack<Character> st = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '*') {
                st.pop();

            } else {
                st.push(ch);
            }
            
            
        }
        String s1 = "";
        while (!st.isEmpty()) {
            s1 += st.pop();
        }
        String s2 = "";
        for (int i = s1.length()-1; i >= 0; i--) {
            s2 += s1.charAt(i);
        }
        return s2;
    }
}