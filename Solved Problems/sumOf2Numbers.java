class sum{
    public static void main(String[] args) {
        int a=9;
        int b = 11;
        System.out.println(sumWithout(a,b));
    }

    public static int sumWithout(int a, int b) {
        while (b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;

        }
        return a;
    }
}