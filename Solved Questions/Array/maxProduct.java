// 1464 - Maximum Product of Two elements in an Array
class maxProduct {
    public static void main(String[] args) {
        int[] a = { 3, 4, 5, 2 };
        System.out.println(product(a));

    }

    public static int product(int[] a) {
        int max1 = Integer.MIN_VALUE;
        int max2 = Integer.MAX_VALUE;
        // int r = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] > max1) {
                max2 = max1;
                max1 = a[i];
            } else if (a[i] > max2) {
                max2 = a[i];
            }
        }
        return max1 * max2;
    }
}