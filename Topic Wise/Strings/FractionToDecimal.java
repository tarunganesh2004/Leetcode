// Fraction To Decimal LC 166

import java.util.*;

class FractionToDecimal{
    public static void main(String[] args) {
        int numerator = 4;
        int denominator = 333;
        System.out.println(fractiontodecimal(numerator, denominator));
    }

    public static String fractiontodecimal(int n, int d) {
        if (n == 0) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        // sign 
        if ((n > 0 && d < 0) || (n < 0 && d > 0)) {
            sb.append("-");
        }
        n = Math.abs(n);
        d = Math.abs(d);

        // integral part
        sb.append(n/d);
        // remainder
        int r = n % d;
        if (r==0){
            return sb.toString();
        }

        // decimal part 
        sb.append(".");
        Map<Integer, Integer> map = new HashMap<>();

        while(r!=0){
            if(map.containsKey(r)){
                int index=map.get(r);
                sb.insert(index,"(");
                sb.append(")");
                break;
            }
            map.put(r,sb.length());
            r *= 10;
            sb.append(r/d);
            r %= d;
        }
        return sb.toString();
    }
}