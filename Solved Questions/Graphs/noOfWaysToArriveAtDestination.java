// LC 1976. Number of Ways to Arrive at Destination
import java.util.*;

class Node implements Comparable<Node> {
    int dest;
    long time;

    public Node(int dest, long time) {
        this.dest = dest;
        this.time = time;
    }

    public int compareTo(Node n1) {
        return Long.compare(this.time, n1.time);
    }
}

class numberOfWaysToArriveAtDestination {
    static int mod = 1000000007;

    public static void main(String[] args) {
        int[][] roads = { { 0, 6, 7 }, { 0, 1, 2 }, { 1, 2, 3 },{1,3,3},LC { 6, 3, 3 }, { 3, 5, 1 }, { 6, 5, 1 }, { 2, 5, 1 },
                { 0, 4, 5 }, { 4, 6, 2 } };
        int n = 7;
        System.out.println(countPaths(n, roads));
    }

    public static int countPaths(int n, int[][] roads) {
        long[] dist = new long[n];
        int[] pathCount = new int[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0;
        pathCount[0] = 1;

        List<Node>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] r : roads) {
            int src = r[0], dest = r[1], time = r[2];
            graph[src].add(new Node(dest, time));
            graph[dest].add(new Node(src, time)); // undirected graph
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(0, 0));
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int u = cur.dest;
            long time = cur.time;

            if (time > dist[u]) {
                continue;
            }

            for (Node neighbour : graph[u]) {
                int v = neighbour.dest;
                long newTime = time + neighbour.time;
                if (newTime < dist[v]) {
                    dist[v] = newTime;
                    pq.add(new Node(v, newTime));
                    pathCount[v] = pathCount[u];
                } else if (newTime == dist[v]) {
                    pathCount[v] = (pathCount[v] + pathCount[u]) % mod;
                }
            }
        }
        return pathCount[n - 1];
    }
}

    // public static int numberOfWays(int n, int[][] roads) {
    //     List<int[]>[] graph = new ArrayList[n];
    //     for (int i = 0; i < n; i++) {
    //         graph[i] = new ArrayList<>();
    //     }
    //     for (int[] edge : roads) {
    //         int src = edge[0], dest = edge[1], time = edge[2];
    //         graph[src].add(new int[] { dest, time });
    //         graph[dest].add(new int[] { src, time });
    //     }
    //     return shortestPath(graph, 0, n);
    // }

    // private static int shortestPath(List<int[]>[] graph, int src, int target) {
    //     // Apply Dijkstra's algorithm
    //     PriorityQueue<long[]> pq = new PriorityQueue<long[]>((a, b) -> Long.compare(a[1],b[1]));
    //     long[] minCost = new long[target];
    //     Arrays.fill(minCost, Long.MAX_VALUE);

    //     long[] ways = new long[target];
    //     ways[0] = 1;
    //     minCost[0] = 0;
    //     pq.add(new long[] { 0, 0 });
    //     while (!pq.isEmpty()) {
    //         long[] current = pq.poll();

    //         int city =(int) current[0];
    //         long curCost = current[1];

    //         if (curCost > minCost[city]) {
    //             continue;
    //         }
    //         for (int[] neighbourData : graph[city]) {
    //             int neighbour = neighbourData[0];
    //             int time = neighbourData[1];
    //             if (curCost + time < minCost[neighbour]) {
    //                 minCost[neighbour] = curCost + time;
    //                 pq.add(new long[] {(long)neighbour, minCost[neighbour] });
    //                 ways[neighbour] = ways[city];
    //             } else if (curCost + time == minCost[neighbour]) {
    //                 ways[neighbour] = (ways[neighbour] + ways[city]) % mod;
    //             }
    //         }
    //     }
    //     return (int) ways[target - 1];
    // }
    
// }