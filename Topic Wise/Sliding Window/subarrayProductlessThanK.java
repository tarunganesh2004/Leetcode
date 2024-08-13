class subarrayProductlessThanK {
    public static void main(String[] args) {
        int[] a = { 10, 5, 2, 6 };
        int k = 100;
        System.out.println(lessthank(a,k));
    }

    public static int lessthank(int[] a,int k) {
        if (k <= 1)
            return 0;
        int c = 0;
        int left = 0;
        int product = 1;
        for (int right = 0; right < a.length; right++) {
            product = product * a[right];
            
            while (product >= k && left <= right) { // increase the left pointer if the product is greater than k
                product = product / a[left];
                left++;
            }
            c = c + (right - left + 1);
        }
        return c;
    }
}