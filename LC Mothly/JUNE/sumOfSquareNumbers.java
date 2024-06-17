public class sumOfSquareNumbers {
    public static void main(String[] args) {
        int c = 5;
        Boolean b = sumOfSquares(c);
        System.out.println(b);
        System.out.println(isPerfect(c));
    }

    public static boolean sumOfSquares(int c) {
        // O(Sqrt(c))
        for (int a = 0; a <= Math.sqrt(c); a++) {
            int b1 = c - a * a; // a^2+b^2=c
            int b = (int) (Math.sqrt(b1));
            if (b * b == b1) {
                return true;
            }
        }
        return false;
    }
    
    public static boolean isPerfect(int c) {
        long s = 0;
        long e = (long) (Math.sqrt(c));
        while (s <= e) {
            long mid = s * s + e * e;
            if (mid == (long) c) {
                return true;
            } else if (mid > (long) c) {
                e--;
            } else {
                s++;
            }
        }
        return false;
    }
}
