class longestPalindromcsubstring {
    public static void main(String[] args) {
        String s = "abc";
        System.out.println(isPalindrome(s));
    }

    public static String findSubstrings(String s) {
        int n=s.length();
        int maxLength = 0;
        String longestPalindrome="";
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                String s1 = s.substring(i, j);
                if (isPalindrome(s1) && s1.length() > longestPalindrome.length()) {
                    int len = s1.length();
                    if (len > maxLength) {
                        maxLength = len;
                    }
                }
            }

        }
        return longestPalindrome;
    }
    public static boolean isPalindrome(String s) {
        // int n = s.length();
        // String s1 = "";
        // for (int i = n - 1; i >= 0; i--) {
        //     s1 += s.charAt(i);
        // }
        // if (s.equals(s1)) {
        //     return true;
        // } else {
        //     return false;
        // }
        // efficient method
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}