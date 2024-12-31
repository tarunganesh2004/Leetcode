import java.util.*;
class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums);
        return nums;
    }

    public void mergeSort(int[] array) {
        int n = array.length;
        if (n <= 1)
            return;

        int mid = n / 2;
        int[] leftArray = Arrays.copyOfRange(array, 0, mid);
        int[] rightArray = Arrays.copyOfRange(array, mid, n);

        mergeSort(leftArray);
        mergeSort(rightArray);
        mergeSortHelper(leftArray, rightArray, array);
    }

    public void mergeSortHelper(int[] leftArray, int[] rightArray, int[] array) {
        int leftSize = leftArray.length;
        int rightSize = rightArray.length;
        int i = 0, j = 0, k = 0;

        // Merge the two subarrays into the original array
        while (i < leftSize && j < rightSize) {
            if (leftArray[i] <= rightArray[j]) {
                array[k++] = leftArray[i++];
            } else {
                array[k++] = rightArray[j++];
            }
        }

        // Copy the remaining elements of leftArray, if any
        while (i < leftSize) {
            array[k++] = leftArray[i++];
        }

        // Copy the remaining elements of rightArray, if any
        while (j < rightSize) {
            array[k++] = rightArray[j++];
        }
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = { 5, 1, 2, 3, 6, 4 };
        s.sortArray(nums);
        System.out.println(Arrays.toString(nums));
    }
}