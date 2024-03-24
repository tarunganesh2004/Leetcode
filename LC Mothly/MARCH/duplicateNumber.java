import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class duplicateNumber {
    public static void main(String[] args) {
        int[] a = { 1, 3, 4, 2, 2 };
        int r = duplicate(a);
        int res = findDuplicate(a);
        System.out.println(r);
        System.out.println(res);
    }

    public static int duplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        int d = 0;
        for (int num : map.keySet()) {
            if (map.get(num) > 1) {
                d = num;
            }
        }
        return d;
    }

    public static int findDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return num;
            }
            set.add(num);
        }
        return -1;
    }

}
