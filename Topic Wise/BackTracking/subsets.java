import java.util.*;
class subsets{
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };
        // int n = arr.length;
        // for(int i=0;i<(1<<n);i++){
        //     for(int j=0;j<n;j++){
        //         if((i & (1<<j))>0){
        //             System.out.print(""+arr[j]+" ");
        //         }
        //     }
        //     System.out.println();
        // }
        List<List<Integer>> res = generate(arr);
        for (List<Integer> l : res) {
            System.out.println(l);
        }
    }

    public static List<List<Integer>> generate(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), nums, 0);
        return res;
    }

    private static void backtrack(List<List<Integer>> l, List<Integer> subset, int[] nums, int start) {
        l.add(new ArrayList<>(subset));
        for (int i = start; i < nums.length; i++) {
            subset.add(nums[i]);
            backtrack(l, subset, nums, i + 1);
            subset.remove(subset.size() - 1);
        }
    }
}