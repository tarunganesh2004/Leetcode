// leetcode 2610
import java.util.HashMap;
import java.util.*;
public class convertArrayto2DArray {
    public static void main(String[] args) {
        int[] a = { 1, 3, 4, 1, 2, 3, 1 };
        List<List<Integer>> l = convert(a);
        System.out.println(l);
    }

    public static List<List<Integer>> convert(int[] a) {
        List<List<Integer>> res = new ArrayList<>();
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : a) {
            if (freq.containsKey(num)) {
                freq.put(num, freq.get(num) + 1);
            } else {
                freq.put(num, 1);
            }
        }
        return res;
    }
    
}
