import java.util.Arrays;

public class burstBaloons {

    public static int minArrowsToBurst(int[][] points) {
        if (points.length == 0)
            return 0;

        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1])); 

        int minArrowPos = points[0][1];
        int count = 1;
        for (int i = 1; i < points.length; i++) {
            if (minArrowPos >= points[i][0]) {
                continue;
            }
            count++; 
            minArrowPos = points[i][1];
        }
        return count; 
    }

    public static void main(String[] args) {
    }
}
