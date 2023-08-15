class Solution {
    public boolean isPalindrome(String s) {
        char[] str = s.toCharArray();

        int i = 0;
        int j = str.length - 1;

        while (i < j) {
            while (i < j && !isLetter(str[i])) {
                i++;
            }

            while(i < j && !isLetter(str[j])) {
                j--;
            }

            if (i < j) {
                 if (Character.toLowerCase(str[i]) == Character.toLowerCase(str[j])) {
                    i++;
                    j--;
                    continue;
                } else {
                    return false;
                }
            } 


        }   

        return true;
    }

    private boolean isLetter(char c) {
        return ('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z' ) || ('0' <= c && c <= '9' );
    }
}