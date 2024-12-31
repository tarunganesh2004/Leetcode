class lastword{
    public static void main(String[] args) {
        String s = "Hello World";
        String s1 = "   fly me to the last moon    ";
        System.out.println(lengthOfLastWord(s));
        System.out.println(lengthOfLastWord(s1));
        System.out.println(anotherway(s));
    }

    public static int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        if (words.length == 0)
            return 0;
        return words[words.length - 1].length();
    }

    public static int anotherway(String s) {
        int length = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ' && length > 0) {
                return length;
            } else if (s.charAt(i) != ' ') {
                length++;
            }
        }
        return length;
    }
}