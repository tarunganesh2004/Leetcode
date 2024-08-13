// LC 1423 , https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class maximumPoints{
    public static void main(String[] args) {
        int[] cardPoints = { 1, 2, 3, 4, 5, 6, 1 };
        int k = 3;
        System.out.println(maxScore(cardPoints, k));
    }

    public static int maxScore(int[] a, int k) {
        int n = a.length;
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum += a[i];
        }
        if (a.length == k)
            return totalSum;
        
        int minSubArraySum = 0;
        for (int i = 0; i < n - k; i++) {
            minSubArraySum += a[i];
        }

        int currentSubArraySum = minSubArraySum;
        for (int i = n - k; i < n; i++) {
            currentSubArraySum = currentSubArraySum - a[i - (n - k)] + a[i];
            minSubArraySum = Math.min(minSubArraySum, currentSubArraySum);
        }
        return totalSum - minSubArraySum;
    }
}