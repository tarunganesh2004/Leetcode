class scoreOfaString{
    public static void main(String[] args) {
        String s = "hello";
        
        System.out.println(score(s));
    }

    public static int score(String s) {
        char[] c = s.toCharArray();
        int score = 0;
        for (int i = 0; i < c.length-1; i++) {
            score += Math.abs(c[i] - c[i + 1]);
        }
        
        return score;
    }
}