public class countTriplets {
    public static void main(String[] args) {
        int[] a = { 2, 3, 1, 6, 7 };
       System.out.println(counttriplets(a));
    }
    
    public static  int counttriplets(int[] nums) {

        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            int xor = 0;
            for (int j = i; j < nums.length; j++) {
                xor ^= nums[j];
                if (xor == 0)
                    count += (j - i);
            }
        }

        return count;
    }
}
