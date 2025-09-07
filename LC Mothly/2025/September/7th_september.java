// find n unique integers sum up to 0 LC 1304(Easy)

class test {
    public static void main(String[] args) {
        int n = 5;
        int[] res = sumZero(n);
        for (int r : res) {
            System.out.print(r + " ");
        }
    }

    public static int[] sumZero(int n) {
        int[] res = new int[n];
        int idx = 0;
        for (int i = 1; i <= n / 2; i++) {
            res[idx++] = i;
            res[idx++] = -i;
        }
        if(n%2==1) res[idx]=0;
        return res;
    }
}