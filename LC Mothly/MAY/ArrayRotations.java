import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class ArrayRotations {

    // Method to rotate the array to the right by one position
    public static int[] rotateArray(int[] array) {
        int n = array.length;
        int[] rotatedArray = new int[n];

        // Move the last element to the first position
        rotatedArray[0] = array[n - 1];

        // Shift all other elements to the right by one position
        for (int i = 1; i < n; i++) {
            rotatedArray[i] = array[i - 1];
        }

        return rotatedArray;
    }

    // Method to generate all rotated arrays
    public static int generateRotatedArrays(int[] array) {
        List<Integer> l = new ArrayList<>();
        int n = array.length;
        int[] currentArray = array.clone(); // Start with the original array

        // Print the original array
        // System.out.println(Arrays.toString(currentArray));

        // Generate and print each rotated version of the array
        for (int i = 1; i < n; i++) {
            currentArray = rotateArray(currentArray);
            int s = sum(currentArray);
            l.add(s);

            // System.out.println(Arrays.toString(currentArray));
        }
        Collections.sort(l);
        return l.get(l.size() - 1);
        
    }

    public static int sum(int[] a) {
        int s = 0;
        int j = 0;
        for (int i = 0; i < a.length; i++) {
            s += (j) * a[i];
            j++;
        }
        return s;
    }

    public static void main(String[] args) {
        int[] array = { 4, 3, 2, 6 };
        System.out.println(generateRotatedArrays(array));
    }
}
