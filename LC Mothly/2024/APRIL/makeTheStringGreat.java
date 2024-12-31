import java.util.Stack;

public class makeTheStringGreat {
    public static void main(String[] args) {
        String s = "leEeetcode";
        System.out.println(great(s));
    }

    public static String great(String s) {
        Stack<Character> st = new Stack<>();
        String res = "";
        st.push(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            if (!st.isEmpty() && Math.abs(st.peek() - s.charAt(i)) == 32) {
                st.pop();
            } else {
                st.push(s.charAt(i));
            }
        }
        for (int i = st.size(); i > 0; i--) {
            res = st.pop() + res;
        }
        // while(!st.isEmpty()){ // This is another way to do the above for loop
        //     res = st.pop() + res;}
        return res;
    }
}
