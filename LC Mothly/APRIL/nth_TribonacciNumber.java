class nth_TribonacciNumber {
    public static void main(String[] args) {
        System.out.println(tribonacci(25));
    }

    public static int tribonacci(int n){
        if(n==0) return 0;
        if(n==1||n==2) return 1;
        int a=0;
        int b=1;
        int c=1;
        int t;
        for(int i=3;i<=n;i++){
            t=a+b+c;
            a=b;
            b=c;
            c=t;
        }
        return c;
    }
}