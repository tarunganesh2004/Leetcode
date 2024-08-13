class squareRoot{
    public static void main(String[] args) {
        int n = 841;
        System.out.println(sqrt(n));
    }

    public static int sqrt(int n) {
        int low = 1;
        int high = n;
        int ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (n / mid == mid) {
                return mid;
            }
            if (n / mid > mid) {
                low = mid + 1;
                ans = mid;
            } else {
                high = mid - 1;
            }
        }
        return ans;
      }
}