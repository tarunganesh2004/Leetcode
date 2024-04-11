import java.util.Stack;

public class removeKDigits {
    public static void main(String[] args) {
        String num = "1432219";
        int k = 3;
        System.out.println(removeDigits(num, k));
    }

    public static String removeDigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        for (char digit : num.toCharArray()) {
            while (!stack.isEmpty() && k > 0 && stack.peek() > digit) {
                stack.pop();
                k--;
            }
            stack.push(digit);
        }

        while (k > 0 && !stack.isEmpty()) {
            stack.pop();
            k--;
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        sb.reverse();

        while (sb.length() > 0 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }

        if (sb.length() > 0) {
            return sb.toString();
        } else {
            return "0";
        }
    }

    // Optimized version
    public static String removedigitsOptimized(String num, int k) {
        char[] digits = num.toCharArray();
        if (k == num.length()) {
            return "0";
        }

        char[] stack = new char[digits.length];
        int stackTop = -1;
        int removalCount = k;

        for (int i = 0; i < digits.length; i++) {
            while (removalCount > 0 && stackTop >= 0 && stack[stackTop] > digits[i]) {
                stackTop--;
                removalCount--;
            }
            stackTop++;
            stack[stackTop] = digits[i];
        }

        int nonZeroStart = 0;

        while (stack[nonZeroStart] == '0' && nonZeroStart < digits.length - k - 1) {
            nonZeroStart++;
        }

        return String.valueOf(stack, nonZeroStart, digits.length - k - nonZeroStart);
    }
}
