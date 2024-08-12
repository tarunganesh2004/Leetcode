// LC 866

class primePalindrome {
    public static void main(String[] args) {
        int n = 12; // o/p: smallest prime which is a palindrome and >=n --> 101 
        System.out.println(getPP(n));
    }

    public static int getPP(int n) {
        // we dont have any even size palindrome(since  it is divisble by 11, except 11)

        int no = (n == 1) ? 2 : n;
        while (true) {
            if ((no > 1e3 && no < 1e4) || (no > 1e5 && no < 1e6) || (no > 1e7 && no < 1e8)) {
                no = (int) Math.pow(10, Math.ceil(Math.log10(no)));
                continue;
            }
            if (checkPrime(no) && isPalindrome(no)) {
                return no;
            }
            no++;
        }
        // return -1;
    }


    // Brute force
    // O(rootn)
    public static boolean checkPrime(int n) {
        boolean isPrime = true;
        if (n == 2)
            return true;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
        return isPrime;
    }

    // O(logn)
    public static boolean isPalindrome(int n) {
        String s = Integer.toString(n);
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
                // break;
            }
            l++;
            r--;
        }
        return true;
    }
}