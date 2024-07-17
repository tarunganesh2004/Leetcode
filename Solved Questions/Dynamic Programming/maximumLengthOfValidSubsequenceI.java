// LC 3201
public class maximumLengthOfValidSubsequenceI {
    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4 };
        System.out.println(longestValid(a)); // Expected output: 4
    }

    public static int longestValid(int[] a) {
        int evenSequence = 0;
        int oddSequence = 0;
        int evenOddSequence = 0;
        int oddEvenSequence = 0;
        for (int x : a) {
            if (x % 2 == 0) {
                evenSequence++;
                evenOddSequence = oddEvenSequence + 1;
            } else {
                oddSequence++;
                oddEvenSequence = evenOddSequence + 1;
            }
        }
        return Math.max(oddSequence, Math.max(evenSequence, Math.max(evenOddSequence, oddEvenSequence)));
    }
}
