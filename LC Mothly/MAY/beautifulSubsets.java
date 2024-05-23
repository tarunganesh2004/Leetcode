    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;

    public class beautifulSubsets {
        public static void main(String[] args) {
            int[] nums = { 2, 4, 6 };
            int k = 2;
            System.out.println(countBeautifulSubsets(nums, k));
        }

        public static int countBeautifulSubsets(int[] nums, int k) {
            int count = 0;
            List<List<Integer>> subsets = generateSubsets(nums);
            for (List<Integer> subset : subsets) {
                if (isBeautiful(subset, k)) {
                    count++;
                }
            }
            return count;
        }

        // Using HashMap
        public static boolean isBeautiful1(List<Integer> subset, int k) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int num : subset) {
                if (map.containsKey(num - k) || map.containsKey(num + k)) {
                    return false;
                }
                map.put(num, map.getOrDefault(num, 0) + 1);
            }
            return true;
        }
        //  O(N^2)
        public static boolean isBeautiful(List<Integer> subset, int k) {
            int size = subset.size();
            for (int i = 0; i < size; i++) {
                for (int j = i + 1; j < size; j++) {
                    if (Math.abs(subset.get(j) - subset.get(i)) == k) {
                        return false;
                    }
                }
            }
            return true;
        }

        public static List<List<Integer>> generateSubsets(int[] nums) {
            List<List<Integer>> allSubsets = new ArrayList<>();
            backtrack(allSubsets, new ArrayList<>(), nums, 0);
            return allSubsets;
        }

        public static void backtrack(List<List<Integer>> allSubsets, List<Integer> subset, int[] nums, int start) {
            if (!subset.isEmpty()) { 
                allSubsets.add(new ArrayList<>(subset));
            }
            for (int i = start; i < nums.length; i++) {
                subset.add(nums[i]);
                backtrack(allSubsets, subset, nums, i + 1);
                subset.remove(subset.size() - 1);
            }
        }
    }
