import java.util.PriorityQueue;

class kthLargestElement{
    public static void main(String[] args) {
        int[] a = { 3, 2, 1, 5, 6, 4 };
        int k = 2;
        System.out.println(kthlargest(a, k));
    }

    public static int kthlargest(int[] a, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(k); // min Heap

        for (int n : a) {
            pq.add(n);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        return pq.poll();
    }
}