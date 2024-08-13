import java.util.*;

class kthFactor{
    public static void main(String[] args) {
        int n=7;
        int k = 2;
        System.out.println(kthFactorOfn(n, k));
    }

    public static int kthFactorOfn(int n, int k) {
        if(n<k){
            return -1;
        }
        List<Integer> l = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                l.add(i);
            }
        }
        Collections.sort(l);
        return l.get(k - 1);

    }
}