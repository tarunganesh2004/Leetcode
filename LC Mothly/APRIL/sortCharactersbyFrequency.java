import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class sortCharactersbyFrequency {
    public static void main(String[] args) {
        String s = "Aabb";
        System.out.println(sort(s));
        System.out.println(frequencySort(s));
        
        // System.out.println(mp);
    }

    public static String sort(String s) {
        Map<Character, Integer> mp = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (mp.containsKey(c)) {
                mp.put(c, mp.get(c) + 1);
            } else {
                mp.put(c, 1);
            }
        }
        // Using PriorityQueue
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> mp.get(b) - mp.get(a));
        pq.addAll(mp.keySet());
        while (!pq.isEmpty()) {
            char ch = pq.poll();
            int value = mp.get(ch);
            for (int i = 0; i < value; i++) {
                sb.append(ch);
            }
        }
        return sb.toString();
    }

    public static String frequencySort(String s) {
        char[] str = s.toCharArray();
        int[] freq = new int[128];
        for (int i = 0; i < str.length; i++)
            freq[str[i]]++;
        for (int i = 0; i < str.length;) {
            char cmax = ',';
            for (int j = 0; j < 128; j++) {
                if (freq[j] > freq[cmax])
                    cmax = (char) j;
            }
            while (freq[cmax] != 0) {
                str[i++] = cmax;
                freq[cmax]--;
            }
        }
        return new String(str);
    }
}
