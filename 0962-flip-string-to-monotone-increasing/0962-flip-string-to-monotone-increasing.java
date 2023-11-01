class Solution {
    public int minFlipsMonoIncr(String s) {
        int endWithZero = 0;
        int endWithOne = 0;
        

        for (char c : s.toCharArray()) {
            if (c == '1') {
               endWithOne = Math.min(endWithOne, endWithZero);
               endWithZero++;
            } else {
               endWithOne++;
            }
        }

        return Math.min(endWithZero, endWithOne);
    }
}