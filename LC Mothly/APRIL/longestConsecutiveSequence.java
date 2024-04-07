import java.util.HashSet;
import java.util.Set;

public class longestConsecutiveSequence {
    public static void main(String[] args) {
        int[] a = { 100, 4, 200, 1, 3, 2 };
        System.out.println(longestConsecutive(a));
    }

    public static int longestConsecutive(int[] nums){
        Set<Integer> set = new HashSet<>();
        for (int n : nums) {
            set.add(n);
        }
        int best = 0;
        for (int n : set) {
            if (!set.contains(n - 1)) {
                int m = n + 1;
                while (set.contains(m)) {
                    m++;
                }
                best = Math.max(best, m - n);
            }
        }
        return best;
    }
}
