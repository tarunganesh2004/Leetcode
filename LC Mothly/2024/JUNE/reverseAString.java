import java.util.Arrays;

class reverseAString {
    public static void main(String[] args) {
        char[] s = { 'h', 'e', 'l', 'l', 'o' };
        reverse(s);
    }

    public static void reverse(char[] s) {
        int n = s.length;
        int start = 0;
        int end = n - 1;
        while (start < end) {
            char c = s[start];
            s[start] = s[end];
            s[end] = c;
            start++;
            end--;
        }
        System.out.println(Arrays.toString(s));
    }
}
