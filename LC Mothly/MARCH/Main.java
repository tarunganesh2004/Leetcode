import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int checkDivisibility(ArrayList<Integer> primeNumbers, int[] coord) {
        int start = coord[0];
        int end = coord[1];
        for (int prime : primeNumbers) {
            boolean isDivisible = true;
            for (int i = start; i <= end; i++) {
                if (i == 1 || (i % prime != 0)) {
                    isDivisible = false;
                    break;
                }
            }
            if (isDivisible) {
                return 1;
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the prime numbers array: ");
        int size = scanner.nextInt();
        ArrayList<Integer> primeNumbers = new ArrayList<>();
        System.out.println("Enter the prime numbers:");
        for (int i = 0; i < size; i++) {
            primeNumbers.add(scanner.nextInt());
        }

        System.out.print("Enter the number of coordinates: ");
        int numCoords = scanner.nextInt();
        int[][] coordinates = new int[numCoords][2];
        System.out.println("Enter the coordinates:");
        for (int i = 0; i < numCoords; i++) {
            for (int j = 0; j < 2; j++) {
                coordinates[i][j] = scanner.nextInt();
            }
        }

        for (int[] coord : coordinates) {
            int result = checkDivisibility(primeNumbers, coord);
            System.out.println("Output for (" + coord[0] + ", " + coord[1] + "): " + result);
        }

        scanner.close();
    }
}
