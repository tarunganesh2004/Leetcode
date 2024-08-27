// LC 373
import java.util.*;
class kPairsWithSmallestSums {
    public static void main(String[] args) {
        int[] nums1 = { 1, 2, 6 };
        int[] nums2 = { 3, 3, 5 };
        int k = 3;
        System.out.println(kSmallest(nums1, nums2, k));
    }
    // better approach
    public static List<List<Integer>> kSmallest(int[] a1, int[] a2, int k) {
        List<List<Integer>> r = new ArrayList<>();
        PriorityQueue<int[]> pq=new PriorityQueue<>(new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0] + a[1], b[0] + b[1]);
            }
        });

        // Initialize the heap with pairs from a1 and a2
        for (int i = 0; i < Math.min(a1.length, k); i++) {
            pq.offer(new int[] { a1[i], a2[0], 0 });
        }
        while (k > 0 && !pq.isEmpty()) {
            int[] cur = pq.poll();
            List<Integer> l = new ArrayList<>();
            l.add(cur[0]);
            l.add(cur[1]);
            k--;

            int nextIndex = cur[2];
            if (nextIndex + 1 < a2.length) {
                pq.offer(new int[] { cur[0], a2[nextIndex + 1], nextIndex + 1 });
            }
        }
        return r;
    }
    // brute force (O(n^2logn^2)) // memory limit exceeded
    public static List<List<Integer>> kSmallestBrute(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>((a, b) -> a.get(0) + a.get(1) - b.get(0) - b.get(1));
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                List<Integer> list = new ArrayList<>();
                list.add(nums1[i]);
                list.add(nums2[j]);
                pq.add(list);
            }
        }
        while (k-- > 0 && !pq.isEmpty()) {
            result.add(pq.poll());
        }
        return result;
    }
}