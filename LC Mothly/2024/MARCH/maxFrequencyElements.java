import java.util.HashMap;
import java.util.Map;

public class maxFrequencyElements {
    public static void main(String[] args) {
        int[] a = { 1, 2, 4, 5, 1, 2, 3, 5, 6, 1, 1, 3, 3, 2, 2, 2, 4, 5, 3, 3, 1 };
        Map<Integer, Integer> freq = countFrequencies(a);
        System.out.println(freq);
        System.out.println(freq.values());
    }

    public static Map<Integer, Integer> countFrequencies(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int e : arr) {
            if (freq.containsKey(e)) {
                // increase the count
                freq.put(e, freq.get(e) + 1);
            } else {
                freq.put(e, 1);
            }
        }
        return freq;
    }

    public static int maxfrequencyelements(int nums[]) {
        Map<Integer, Integer> freq = countFrequencies(nums);
        // for maximum frequency
        int maxFreq = 0;
        int count = 0; // count of elements with max frequency
        for (int e : freq.values()) {
            maxFreq = Math.max(maxFreq, e);
        }

        for (int e : freq.values()) {
            if (e == maxFreq) {
                count = count + maxFreq;
            }
        }

        return count;
    }
    // another approach
    public static int maxFrequencyelements(int[] nums) {
        int ans = 0;
        int maxFreq = Integer.MIN_VALUE;
        int[] count = new int[101];
        for (int num : nums) {
            count[num]++;
        }
        for (int num : count) {
            maxFreq = Math.max(maxFreq, num);
        }
        for (int num : nums) {
            if (maxFreq == count[num]) {
                ans++;
            }
        }
        return ans;
    }
}
