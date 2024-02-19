public class mergeAlternative {
    public static void main(String[] args) {
        String s1 = "abc";
        String s2 = "pqr";
System.out.println(mergeAlternatively(s1, s2));
    }

    public static String mergeAlternatively(String s1, String s2) {
        StringBuilder s = new StringBuilder();
        int n = 100;
        for (int i = 0; i < n; i++) {
            if (i < s1.length()) {
                s.append((s1.charAt(i)));
            }
            if (i < s2.length()) {
                s.append((s2.charAt(i)));
            }
        }
        return s.toString();
    }
}