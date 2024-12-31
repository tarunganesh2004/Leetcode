// Problem statement: isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
// For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

// Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

class countPrefixandSuffixPairs {
    public static void main(String[] args) {
       String[] words = { "bc","b","ab" };// doesnt work for this input(Expected: 0, getting Output: 1)
        String[] words1 = { "a", "aba", "ababa", "aa"}; // output: 4
        System.out.println(countPairs(words1));
        System.out.println(countPairs(words));
    }
// correct method
    public static int countPairs(String[] words) {
        int n = words.length;
        int ct = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int ilen = words[i].length(), jlen = words[j].length();

                if (ilen <= jlen) {
                    boolean prefixFlag = words[j].substring(0, ilen).equals(words[i]);
                    boolean postfixFlag = words[j].substring(jlen - ilen).equals(words[i]);
                    if (prefixFlag && postfixFlag) {
                        ct++;
                    }
                }
            }
        }
        return ct;
    }

//     public static int countprefixandsuffixpairs(String[] words) {
//     int c=0;
//     int n = words.length;
//     for (int i = 0; i < n; i++) {
//         for(int j=0;j<n;j++){
//             String s1=words[i];
//             String s2=words[j];
//             if(s2.startsWith(s1)&& s1.endsWith(s2)){
//                 c++;
//             }
//         }
//     }
//     return c;
// }
    // wrong method(not working for some cases)
    static boolean helper(String s1, String s2) {
        int n = s1.length();
        String a = s1.substring(0, n);
        String b = s2.substring(s2.length() - n);

        return a.equals(b);
    }

    public static int countPrefixandsuffix(String[] words) {
        int c = 0;
        for (int i = 0; i < words.length; i++) {
            String s1 = words[i];
            for (int j = i + 1; j < words.length; j++) {
                String s2 = words[j];
                if (s2.length() >= s1.length()) {
                    if (helper(s1, s2))
                        c++;
                }
            }
        }
        return c;
    }

}

// public static void main(String[] args) {
// String[] words = {"abab", "baba", "aba"};
// String prefix = "ab";
// String suffix = "ab";
// System.out.println(countPrefixandsuffix(words, prefix, suffix));
// }

// public static int countPrefixandsuffix(String[] words, String prefix, String
// suffix) {
// int count = 0;
// for (String word : words) {
// if (word.startsWith(prefix) && word.endsWith(suffix)) {
// count++;
// }
// }
// return count;
// }