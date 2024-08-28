// lC problem: 451. Sort Characters By Frequency
import java.util.*;
public class sortCharactersByFrequency {
    public static void main(String[] args) {
        String s = "tree";
        System.out.println(frequencySort(s));
    }
    public static String frequencySort(String s) {
        int[] freq = new int[256];
        for (char c : s.toCharArray()) {
            freq[c]++;
        }
        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> freq[b] - freq[a]);
        for (int i = 0; i < 256; i++) {
            if (freq[i] > 0) {
                pq.offer((char) i);
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            char c = pq.poll();
            for (int i = 0; i < freq[c]; i++) {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
