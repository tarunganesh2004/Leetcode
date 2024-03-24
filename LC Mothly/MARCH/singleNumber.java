import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class singleNumber{
    public static void main(String[] args) {
        int[] a = { 0, 1, 0, 1, 0, 1, 99 };

    }

    public static int singleNumberII(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                int count = map.get(num);
                map.put(num, count + 1);
            } else {
                map.put(num, 1);
            }
        }

        for (int key : map.keySet()) {
            if (map.get(key) == 1) {
                return key;
            }
        }
        return -1;
    }

    public int[] singleNumberIII(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> a=new ArrayList<>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                int count = map.get(num);
                map.put(num, count + 1);
            } else {
                map.put(num, 1);
            }
        }

        for (int key : map.keySet()) {
            if (map.get(key) == 1) {
                a.add(key);
            }
        }
        int[] res = new int[a.size()];
        for (int i = 0; i < a.size(); i++) {
            res[i] = a.get(i);
        }
        return res;
    }
}