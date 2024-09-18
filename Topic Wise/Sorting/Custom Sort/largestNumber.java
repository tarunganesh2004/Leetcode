// LC 179. Largest Number
import java.util.*;

public class largestNumber {
    public static void main(String[] args) {
        int[] a = { 3, 30, 34, 5, 9 };
        String[] s = new String[a.length];
        for (int i = 0; i < a.length; i++) {
            s[i] = String.valueOf(a[i]);
        }
        // System.out.println(Arrays.toString(s));
        // System.out.println(Arrays.toString(s));

        System.out.println(largest(a));
    }

    static String largest(int[] a) {
        String[] s = new String[a.length];
        for (int i = 0; i < a.length; i++) {
            s[i] = String.valueOf(a[i]);
        }
        Arrays.sort(s, (x, y) -> (y + x).compareTo(x + y));
        StringBuilder sb = new StringBuilder();
        for (String i : s) {
            sb.append(i);
        }
        if (sb.charAt(0) == '0') {
            return "0";
        }
        return sb.toString();
    }
}

// public class LargestNumberCustomSort {
//     // Function to swap two elements in an array
//     public static void swap(String[] arr, int i, int j) {
//         String temp = arr[i];
//         arr[i] = arr[j];
//         arr[j] = temp;
//     }

//     // Custom bubble sort function
//     public static void bubbleSort(String[] arr) {
//         int n = arr.length;
//         for (int i = 0; i < n - 1; i++) {
//             for (int j = 0; j < n - i - 1; j++) {
//                 // Compare concatenated pairs (y + x) and (x + y)
//                 if ((arr[j + 1] + arr[j]).compareTo(arr[j] + arr[j + 1]) > 0) {
//                     // Swap if the condition holds (to form the largest number)
//                     swap(arr, j, j + 1);
//                 }
//             }
//         }
//     }

//     public static String largestNumber(int[] nums) {
//         // Convert the array of integers to an array of strings
//         String[] arr = new String[nums.length];
//         for (int i = 0; i < nums.length; i++) {
//             arr[i] = String.valueOf(nums[i]);
//         }

//         // Use custom bubble sort to sort the array based on the concatenation logic
//         bubbleSort(arr);

//         // If the largest number is "0", return "0" (to handle cases like [0, 0])
//         if (arr[0].equals("0"))
//             return "0";

//         // Build the largest number by concatenating the sorted strings
//         StringBuilder largestNum = new StringBuilder();
//         for (String num : arr) {
//             largestNum.append(num);
//         }

//         return largestNum.toString();
//     }

//     public static void main(String[] args) {
//         int[] nums = { 3, 30, 34, 5, 9 };
//         System.out.println(largestNumber(nums)); // Output: "9534330"
//     }
// }
