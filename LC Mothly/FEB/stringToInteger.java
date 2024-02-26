// leetcode : 8. String to Integer 
public class stringToInteger {
    public static void main(String[] args) {
        String s = "       -42";
        String s1 = "4193 with words";
        System.out.println(myAtoi(s));
        System.out.println(myAtoi(s1));
    }

    public static int myAtoi(String s) {
        // removing whitespaces
        s = s.trim();
        if (s.isEmpty()) {
            return 0;
        }

        int ans = 0; // to store the result
        int i = 0; // current index
        boolean neg = s.charAt(0) == '-'; // determines if the variable is + or -
        boolean pos = s.charAt(0) == '+';

        if (neg || pos) {
            i++; // if a sign is present at the beginning of the string,then move to next character
        }

        // Iterating through the string , converting characters to digits
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';

            // for overflow
            if (ans > Integer.MAX_VALUE / 10 || (ans == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) {
                if (neg) {
                    return Integer.MIN_VALUE;
                } else {
                    return Integer.MAX_VALUE;
                }
            }
            ans = ans * 10 + digit;
            i++;
        }
        if (neg) {
            return -ans;
        } else {
            return ans;
        }
    }
}
