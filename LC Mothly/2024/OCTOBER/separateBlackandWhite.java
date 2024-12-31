class Main{
    public static void main(String[] args) {
        String s = "101";
        System.out.println(minSteps(s));
    }
    
    public static  long minSteps(String s) {
        int n = s.length();
        long swaps = 0, zeros = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '1') {
                swaps += zeros;
            } else {
                zeros++;
            }
        }
        return swaps;
    }
}