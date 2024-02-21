class bitwiseAND {
    public static void main(String[] args) {
        int left = 5;
        int right = 7;
        System.out.println(and(left,right));
    }

    public static int and(int left, int right) {
        int shift = 0;
        while (left < right) {
            left = left >> 1;
            right = right >> 1;
            shift++;
        }
        return left << shift;
    }
}