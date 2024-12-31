// LC : 1st March dailyqsn
// Maximum Odd Binary Number

class maximumOddBinaryNumber {
    public static String maxOddBinaryNumber(String s) {
        int c1 = 0;
        int c2 = 0;
        for (char c : s.toCharArray()) {
            if (c == '1')
                c1++;
            else
                c2++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < c1 - 1; i++) {
            sb.append("1");
        }
        for (int i = 0; i < c2; i++) {
            sb.append("0");
        }
        sb.append("1");
        return sb.toString();
    }

    public static void main(String[] args) {
        String s = "0101";
        System.out.println(maxOddBinaryNumber(s));
    }
}