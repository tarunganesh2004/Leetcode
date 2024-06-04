// LC 1338

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
// import java.util.HashSet;
import java.util.List;
import java.util.Map;
// import java.util.Set;

public class reduceArrayToHalf {
    public static void main(String[] args) {
        int[] arr = { 3, 3, 3, 3, 5, 5, 5, 2, 2, 7 };
        System.out.println(reduce(arr));
       
    }

    public static int reduce(int[] arr) {
        Map<Integer,Integer> freq=new HashMap<>();
        // Set<Integer> s=new HashSet<>();
        for (int i = 0; i < arr.length; i++) {
            if (freq.containsKey(arr[i])) {
                freq.put(arr[i], freq.get(arr[i]) + 1);
            } else {
                freq.put(arr[i], 1);
            }
        }
        List<Integer> s = new ArrayList<>();
        for (int x : freq.values()) {
            s.add(x);
        }
        Collections.sort(s);
        int count = 0;
        int sum = 0;
        for (int i = s.size() - 1; i >= 0; i--) {
            sum = sum + s.get(i);
            count++;
            if (sum >= arr.length / 2) {
                break;
            }
        }
        return count;
    }
}
