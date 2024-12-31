// import java.util.Arrays;
import java.util.HashMap;

class longestPalindrome{
    public static void main(String[] args) {
        String s = "aAbccccdd";
        System.out.println(longest(s));
        // int[] freq = new int[52];
        // for (char c : s.toCharArray()) {
        //     if (Character.isLowerCase(c)) {
        //         freq[c - 'a']++;
        //     }
        //     else if (Character.isUpperCase(c)) {
        //         freq[c-'A'+26]++;
        //     }
        // }
        // System.out.println(Arrays.toString(freq));
        
    }

    public static int longest(String s) {
        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (freq.containsKey(c)) {
                freq.put(c, freq.get(c) + 1);
            } else {
                freq.put(c, 1);
            }
        }

        int c=0;
        boolean hasOdd=false;
        for(int i:freq.values()){
            if(i%2==0){
                c+=i;
            }
            else{
                c+=i-1;
                hasOdd=true;
            }
        }
        if(hasOdd){
            c+=1;
        }
        return c;
    }
}