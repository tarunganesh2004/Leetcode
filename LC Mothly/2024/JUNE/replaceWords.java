import java.util.*;

public class replaceWords {
    public static void main(String[] args) {
        List<String> dictionary = new ArrayList<>();
        dictionary.add("cat");
        dictionary.add("bat");
        dictionary.add("rat");

        String sentence = "the cattle was rattled by the battery";
        System.out.println(replace(dictionary, sentence));
    }

    public static String replace(List<String> l,String s){
        String[] s1 = s.split(" ");
        StringBuilder res = new StringBuilder();
        for (String word : s1) {
            // initialize replacement for each word in the sentence
            String replacement = word; 
            // Checking each prefix in the dictionary
            for (String prefix : l) {
                if (word.startsWith(prefix) && prefix.length() < replacement.length()) {
                    replacement = prefix;
                }
            }

            // appending the replacement word to result
            if (res.length() > 0) {
                res.append(" ");
            }
            res.append(replacement);
        }
        
        
        return res.toString();
    }
}
