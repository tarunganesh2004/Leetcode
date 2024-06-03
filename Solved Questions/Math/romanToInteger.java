public class romanToInteger {
    public static void main(String[] args) {
        String s = "III";
        String s1 = "LVIII";
        System.out.println(romantoInt(s1));
    }

    public static int romantoInt(String s) {
        int number = 0;
        int length = s.length();
        for (int i = length - 1; i >= 0; i--) {
            switch (s.charAt(i)) {
                case 'I':
                    number += 1;
                    break;
                case 'V':
                    if (i > 0 && s.charAt(i - 1) == 'I') {
                        number += 4;
                        i--; // Skip the previous 'I'
                    } else {
                        number += 5;
                    }
                    break;
                case 'X':
                    if (i > 0 && s.charAt(i - 1) == 'I') {
                        number += 9;
                        i--; // Skip the previous 'I'
                    } else {
                        number += 10;
                    }
                    break;
                case 'L':
                    if (i > 0 && s.charAt(i - 1) == 'X') {
                        number += 40;
                        i--; // Skip the previous 'X'
                    } else {
                        number += 50;
                    }
                    break;
                case 'C':
                    if (i > 0 && s.charAt(i - 1) == 'X') {
                        number += 90;
                        i--; // Skip the previous 'X'
                    } else {
                        number += 100;
                    }
                    break;
                case 'D':
                    if (i > 0 && s.charAt(i - 1) == 'C') {
                        number += 400;
                        i--; // Skip the previous 'C'
                    } else {
                        number += 500;
                    }
                    break;
                case 'M':
                    if (i > 0 && s.charAt(i - 1) == 'C') {
                        number += 900;
                        i--; // Skip the previous 'C'
                    } else {
                        number += 1000;
                    }
                    break;
                default:
                    throw new IllegalArgumentException("Invalid Roman numeral character");
            }
        }
        return number;

    }
}

