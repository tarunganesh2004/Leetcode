// leetcode 997
public class townJudge {
    public static void main(String[] args) {
        int n = 2;
        int[][] trust = { { 1, 2 } };
        System.out.println(findJudge(n, trust));
    }

    public static int findJudge(int n, int[][] trust) {
        int[] trustcount = new int[n + 1];

        for (int[] relation : trust) {
            trustcount[relation[0]]--;
            trustcount[relation[1]]++;
        }

        for (int i = 1; i <= n; ++i) {
            if (trustcount[i] == n - 1) {
                return i;
            }
        }

        return -1;
    }
}
