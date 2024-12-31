// 13th FEB

public class palindromicString {
    public static void main(String[] args) {
        String[] s = { "abc", "car", "ada", "racecar", "cool" };
        String l = findPalindrome(s);
        System.out.println(l);
    }

    public static boolean check(String s) {
        int i = 0, j = s.length() - 1;
        while (i <= j) {
            if (s.charAt(i) == s.charAt(j)) {
                i++;
                j--;
            } else {
                return false;
            }
        }
        return true;
    }

        public static String findPalindrome(String[] words){
            for(String s:words){
                if(check(s)){
                    return s;
                }
            }
            return "";
        }
    }

