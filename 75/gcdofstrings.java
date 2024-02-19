class gcdofstrings{
    public static void main(String[] args) {
        String str1 = "ABCABC";
        String str2 = "ABC";
        System.out.println(gcdOfStrings(str1, str2));
    }

    public static String gcdOfStrings(String str1, String str2) {
        String s1 = str1 + str2;
        String s2 = str2 + str1;
        if (!s1.equals(s2)) {
            return "";
        }
        int r = gcd(str1.length(), str2.length());
        return str2.substring(0, r);
    }

    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;

        } else {
            return gcd(b, a % b);
        }
    }
}