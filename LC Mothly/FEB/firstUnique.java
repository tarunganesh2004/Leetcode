// FEB - 11

// First unique character in a string and return its index

// import java.util.Arrays;

class firstUnique {
    public static void main(String[] args) {
        String s = "eetcode";
        int i = findUnique(s);
        System.out.println(i);
    }

    public static int findUnique(String s) {
        int[] charCount = new int[26]; // creates an array of 26 elements(for 26 characters)
        for (char c : s.toCharArray()) {
            charCount[c - 'a']++;// increment the count of the character
            for(int i = 0; i < charCount.length; i++) {
                System.out.print(charCount[i]+" ");
            }
        }
        for (int i = 0; i < s.length(); i++) {
            if (charCount[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    } 
}