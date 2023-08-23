class Solution {
    public String breakPalindrome(String palindrome) {
        if (palindrome.length() == 1) {
            return "";
        }
        char[] strs = palindrome.toCharArray();

        for (int i = 0; i < strs.length / 2; i++) {
            if (strs[i] != 'a') {
                strs[i] = 'a';
                return new String(strs);
            }
        }

        strs[strs.length - 1] = 'b';
        return new String(strs);
    }
}