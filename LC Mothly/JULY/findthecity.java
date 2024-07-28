// Leetcode 1334, July 26

import java.util.*;

class findthecity {
    class edge {
        int src;
        int dest;
        int weight;

        edge(int src, int dest, int weight) {
            this.src = src;
            this.dest = dest;
            this.weight = weight;
        }
    }

    class pair {
        int weight;
        int src;

        pair(int a, int b) {
            this.weight = a;
            this.src = b;
        }
    }

    public static int findtheCity(int n, int[][] edges, int hold) {
        List<List<edge>> l = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            l.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            l.get(e[0]).add(new edge(e[0], e[1], e[2]));
            l.get(e[1]).add(new edge(e[1], e[0], e[2]));
        }
        int ans = Integer.MAX_VALUE;
        int city = -1;
        for (int i = 0; i < n; i++) {
            PriorityQueue<pair> p = new PriorityQueue<>((a, b) -> (a.weight - b.weight));
            p.add(new pair(0, i));

            int[] dis = new int[n];
            Arrays.fill(dis, Integer.MAX_VALUE);
            dis[i] = 0;
            boolean[] visited = new boolean[n];

            while (!p.isEmpty()) {
                pair t = p.poll();
                int u = t.src;
                if (visited[u]) {
                    continue;
                }
                visited[u] = true;
                for (edge e : l.get(u)) {
                    int v = e.dest;
                    if (!visited[v] && dis[u] + e.weight < dis[v]) {
                        dis[v] = dis[u] + e.weight;
                        p.add(new pair(dis[v], v));
                    }
                }
            }
            int reach = 0;
            for (int d : dis) {
                if (d <= hold) {
                    reach++;
                }
            }
            if (reach <= ans) {
                ans = reach;
                city = i;
            }
        }
        return city;
    }
}
