import java.util.*;

public class Main {
    // static int[] num = { 1, 2, 3 };

    public static void main(String[] args) {
        int[] num = { 1, 2, 3 };
        int n = num.length;
        for (int t = 1; t <= n; t++) {
            int[] arr = new int[t];
            r(t, arr, num,0,0);
        }
    }

    public static void r(int t, int[] arr,int[] num, int index,int low) {
        if (index == t) {
            System.out.print(Arrays.toString(arr)+" ");
            return;
        }
        for (int i = low; i < num.length;i++) {
            arr[index] = num[i];
            r(t, arr, num,index + 1,i+1);
        }
    }
}
