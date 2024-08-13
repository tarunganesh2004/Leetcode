public class MaxPointsOnLine {

    public static int maxPoints(int[][] points) {
        int n = points.length;
        if (n <= 1) {
            return n;
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            int count = 1; // count the current point
            double slope = Double.POSITIVE_INFINITY; // handle duplicates and same x-coordinates

            for (int j = i + 1; j < n; j++) {
                if (points[i][0] == points[j][0]) {
                    slope = Double.POSITIVE_INFINITY; // all points with same x-coordinate have infinite slope
                } else {
                    // Calculate slope as double to avoid integer division issues
                    slope = (double) (points[i][1] - points[j][1]) / (points[i][0] - points[j][0]);
                }

                int cnt = 2; // considering the current point and the point being compared
                for (int k = j + 1; k < n; k++) {
                    // Check if the kth point falls on the line with slope calculated earlier
                    if (points[k][1] - points[i][1] == slope * (points[k][0] - points[i][0])) {
                        cnt++;
                    }
                }
                result = Math.max(result, cnt);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[][] points = { { 1, 1 }, { 2, 2 }, { 3, 3 } };
        System.out.println(maxPoints(points));
    }
}
