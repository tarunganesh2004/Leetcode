public class reverseVowels {
    public static void main(String[] args) {
        String s = "hello";
        System.out.println(reversevowels(s));
    }

    public static String reversevowels(String s) {
        if (s == null || s.length() == 0)
            return s;
        char[] c = s.toCharArray();
        int left = 0;
        int right = c.length-1;
        String vowels = "aeiouAEIOU";

        while (left < right) {
            // move the left pointer until vowel is found
            while (left < right && !vowels.contains(c[left] + "")) {
                left++;
            }
            // move the right pointer until vowel is found
            while (left < right && !vowels.contains(c[right] + "")) {
                right--;
            }

            // swap the vowels
            if (left < right) {
                char temp = c[left];
                c[left] = c[right];
                c[right] = temp;
                left++;
                right--;
            }
        }
        return new String(c);
    }
}
