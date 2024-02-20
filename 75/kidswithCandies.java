import java.util.ArrayList;
import java.util.List;

public class kidswithCandies {
    public static void main(String[] args) {
        int[] candies = { 2, 3, 5, 1, 3 };
        int extraCandies = 3;
        System.out.println(kidswithcandies(candies, extraCandies));
    }

    public static List<Boolean> kidswithcandies(int[] candies, int extraCandies) {
        List<Boolean> ll = new ArrayList<>();
        int maxcandies = 0;
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] > maxcandies) {
                maxcandies = candies[i];
            }
        }
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= maxcandies) {
                ll.add(true);
            } else {
                ll.add(false);
            }
        }
        return ll;
    }
}
