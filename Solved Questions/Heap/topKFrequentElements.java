// LC 347 Top K Frequent Elements

import java.util.*;

public class topKFrequentElements {
    public static void main(String[] args) {
        int[] a = { 1, 1, 1, 2, 2, 3 };
        int k = 2;
        System.out.println(Arrays.toString(topKFrequent(a, k)));
    }

    public static int[] topKFrequent(int[] a, int k) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int n : a) {
            m.put(n, m.getOrDefault(n, 0) + 1);
        }

        // initialize priority queue with less frequent element at the top
        PriorityQueue<Integer> pq = new PriorityQueue<>(k, (n1, n2) -> m.get(n1) - m.get(n2));

        for (int n : m.keySet()) {
            pq.add(n);
            if (pq.size() > k) {
                pq.poll();
            }
        }

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = pq.poll();
        }
        return res;
    }
}
