// LC 1976. Number of Ways to Arrive at Destination
import java.util.*;

// class edge {
//     int src, dest, weight;
//     edge(int src, int dest, int weight) {
//         this.src = src;
//         this.dest = dest;
//         this.weight = weight;
//     }
// }

class numberOfWaysToArriveAtDestination {
    static int mod = 1000000007;
    public static void main(String[] args) {
        int[][] roads = { { 0, 6, 7 }, { 0, 1, 2 }, { 1, 2, 3 }, { 6, 3, 3 }, { 3, 5, 1 }, { 6, 5, 1 }, { 2, 5, 1 },
                { 0, 4, 5 }, { 4, 6, 2 } };
        int n = 7;
        numberOfWays(n, roads);
    }

    public static int numberOfWays(int n, int[][] roads) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : roads) {
            int src = edge[0], dest = edge[1], time = edge[2];
            graph[src].add(new int[] { dest, time });
            graph[dest].add(new int[] { src, time });
        }
        return shortestPath(graph, 0, n);
    }

    private static int shortestPath(List<int[]>[] graph, int src, int target) {
        // Apply Dijkstra's algorithm
        PriorityQueue<long[]> pq = new PriorityQueue<long[]>((a, b) -> Long.compare(a[1],b[1]));
        long[] minCost = new long[target];
        Arrays.fill(minCost, Long.MAX_VALUE);

        long[] ways = new long[target];
        ways[0] = 1;
        minCost[0] = 0;
        pq.add(new long[] { 0, 0 });
        while (!pq.isEmpty()) {
            long[] current = pq.poll();

            int city =(int) current[0];
            long curCost = current[1];

            if (curCost > minCost[city]) {
                continue;
            }
            for (int[] neighbourData : graph[city]) {
                int neighbour = neighbourData[0];
                int time = neighbourData[1];
                if (curCost + time < minCost[neighbour]) {
                    minCost[neighbour] = curCost + time;
                    pq.add(new long[] {(long)neighbour, minCost[neighbour] });
                    ways[neighbour] = ways[city];
                } else if (curCost + time == minCost[neighbour]) {
                    ways[neighbour] = (ways[neighbour] + ways[city]) % mod;
                }
            }
        }
        return (int) ways[target - 1];
    }
    
}