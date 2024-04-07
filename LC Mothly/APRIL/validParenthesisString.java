import java.util.Stack;

class validParenthesisString {
    public static void main(String[] args) {
        String s="(*)";
        System.out.println(checkValidString(s));
    }

    public static boolean checkValidString(String s) {
        int leftMin = 0;
        int leftMax = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                leftMin++;
                leftMax++;
            } else if (c == ')') {
                leftMin--;
                leftMax--;
            } else {
                leftMin--;
                leftMax++;
            }
            if (leftMax < 0)
                return false;
            if (leftMin < 0) {
                leftMin = 0;
            }
        }
        return leftMin == 0;
    }

    // Using Stack
    public static boolean checkValidStringUsingStack(String s) {
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> starIndex = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else if (c == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else if (!starIndex.isEmpty()) {
                    starIndex.pop();
                } else {
                    return false;
                }
            } else {
                starIndex.push(i);
            }
        }

        while (!stack.isEmpty()) {
            if (!starIndex.isEmpty() && stack.peek() < starIndex.peek()) {
                stack.pop();
                starIndex.pop();
            } else {
                return false;
            }

        }
        return true;
    }
}