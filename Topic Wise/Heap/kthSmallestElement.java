import java.util.*;
public class kthSmallestElement {
    public static void main(String[] args) {
        int[] a = { 3, 2, 1, 5, 6, 4 };
        int k = 2;
        System.out.println(kthsmallest(a, k));
    }

    public static int kthsmallest(int[] a, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder()); // max Heap

        for (int n : a) {
            pq.add(n);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        return pq.poll();
    }
}
