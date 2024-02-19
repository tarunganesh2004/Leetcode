// FEB-19 
// binary form of 2 power any number is 1 followed by n number of 0's(0b100...) and 
// binary form of 2 power any number minus 1 is n number of 1's(0b111...)
// so, if we do bitwise and of n and n-1, it will be 0 if n is power of 2
// for any number n > 0
// n & n - 1 removes the last 1 in the binary form of n
// if and only if n is a power of two, there is only one 1 in the binary form of n
// so, n & n - 1 will be 0 if n is a power of two

class powerOfTwo{
    public static void main(String[] args) {
        int n = 16;
        System.out.println(findPower(n));
        System.out.println(findPower2(n));
        System.out.println(findpower(n));
        System.out.println(findPowerof2(n));
    }

    public static boolean findPower(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }

    public static boolean findPower2(int n) {
        return n > 0 && (n & -n) == n;
    }

    public static boolean findpower(int n) {
        return n > 0 && Integer.bitCount(n) == 1;
    }

    public static boolean findPowerof2(int n) {
        if (n == 0)
            return false;
        while (n % 2 == 0) {
            n = n / 2;
        }
        return n == 1;
    }
}