// convert Integer to the sum of two no-zero Integers LC 1317(Easy)

// import java.util.*;

class September8th {
    public static void main(String[] args) {
        int n = 2;
        System.out.println(convert(n));
    }

    public static int[] convert(int n) {
        n--;
        int m = 1;
        int ans[] = { m, n };

        while (contains(ans[0]) == true || contains(ans[1]) == true) {
            ans[0]++;
            ans[1]--;
        }

        return ans;
    }
    
    public static boolean contains(int n){
        // boolean flag = false;
        while (n != 0) {
            if(n%10==0) return true;
            n=n/10;
        }
        return false;
    }
}
