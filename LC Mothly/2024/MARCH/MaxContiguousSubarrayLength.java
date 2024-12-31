import java.util.HashMap;

public class MaxContiguousSubarrayLength {
    // Method to generate all subarrays
    public static int[][] generateSubarrays(int[] nums) {
        int n = nums.length;
        int totalSubarrays = n * (n + 1) / 2;
        int[][] subarrays = new int[totalSubarrays][];
        int index = 0;

        // Iterate through all possible start indices
        for (int start = 0; start < nums.length; start++) {
            // Iterate through all possible end indices
            for (int end = start; end < nums.length; end++) {
                int subarraySize = end - start + 1;
                subarrays[index] = new int[subarraySize];
                // Copy elements from start to end index to the subarray
                for (int i = start, j = 0; i <= end; i++, j++) {
                    subarrays[index][j] = nums[i];
                }
                index++;
            }
        }
        return subarrays;
    }

    // Method to count the number of zeros in each subarray
    public static int[] countZeros(int[][] subarrays) {
        int[] zerosCount = new int[subarrays.length];
        for (int i = 0; i < subarrays.length; i++) {
            for (int j = 0; j < subarrays[i].length; j++) {
                if (subarrays[i][j] == 0) {
                    zerosCount[i]++;
                }
            }
        }
        return zerosCount;
    }

    // Method to count the number of ones in each subarray
    public static int[] countOnes(int[][] subarrays) {
        int[] onesCount = new int[subarrays.length];
        for (int i = 0; i < subarrays.length; i++) {
            for (int j = 0; j < subarrays[i].length; j++) {
                if (subarrays[i][j] == 1) {
                    onesCount[i]++;
                }
            }
        }
        return onesCount;
    }

    // Method to check if the number of zeros equals the number of ones in each
    // subarray
    public static int findMaxLength(int[] nums) {
        int[][] subarrays = generateSubarrays(nums);
        int[] zerosCount = countZeros(subarrays);
        int[] onesCount = countOnes(subarrays);

        int maxLength = 0;
        for (int i = 0; i < subarrays.length; i++) {
            if (zerosCount[i] == onesCount[i]) {
                maxLength = Math.max(maxLength, subarrays[i].length);
            }
        }
        return maxLength;

        // This is a brute force approach and has a time complexity of O(n^3) , it doesnt work for large inputs
    }

    // Another approach
    public static int maxLength(int[] nums) {
        int n = nums.length;
        int sum = 0;
        int subArrayLength = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                sum += -1;
            } else {
                sum += 1;
            }
            if (sum == 0) {
                subArrayLength = i + 1;
            }
            if (map.containsKey(sum)) {
                subArrayLength = Math.max(subArrayLength, i - map.get(sum));
            } else {
                map.put(sum, i);
            }
        }
        return subArrayLength;
    }


    public static void main(String[] args) {
        int[] nums = { 0, 1, 0, 1, 0, 1 };
        System.out.println(
                "Maximum length of contiguous subarray with equal number of 0s and 1s: " + findMaxLength(nums));
    }
}
