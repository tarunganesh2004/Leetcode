// sum of two numbers without using(+) operator

public class sumOfTwoNumbers {
    public static void main(String[] args) {
        int a = 2;
        int b = 3;
        System.out.println(getSum(a, b));
    }

    public static int getSum(int a, int b) {
        int carry = 0;
        while (b != 0) {
            carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}
