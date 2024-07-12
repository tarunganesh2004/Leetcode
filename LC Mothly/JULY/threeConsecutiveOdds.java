class threeConsecutiveOdds{
    public static void main(String[] args) {
        int[] a = { 2, 6, 4, 1 };
        System.out.println(threeConsecutive(a));
    }

    public static boolean threeConsecutive(int[] a) {
        int n = a.length;
        for (int i = 0; i < n - 2; i++) {
            int r = a[i] * a[i + 1] * a[i + 2];
            if (r % 2 != 0) {
                return true;
            }
        }
        return false;
    }
}