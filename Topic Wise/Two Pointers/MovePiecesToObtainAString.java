 // LC 2337 You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

// The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
// The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
// Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

class MovePiecesToObtainAString{
    public static void main(String[] args) {
        String start = "_L__R__R_";
        String target = "L______RR";
        System.out.println(canChange(start, target));
    }

    public static boolean canChange(String start, String target) {
        int n = start.length();
        int i = 0;
        int j = 0;
        
    }
}