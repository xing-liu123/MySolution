class Solution {
    public boolean validPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        boolean used = false;
        while (left < right) {
            if (s.charAt(left) == s.charAt(right)) {
                left++;
                right--;
            } else if (!used) {
                if(left == right - 1) {
                    return true;
                } else {
                     boolean b1 = helper(s, left + 1, right);
                     boolean b2 = helper(s, left, right - 1);
                     return b1 || b2;
                }
            } else {
                return false;
            }
        }

        return true;
    }

    private boolean helper(String s, int left, int right) {
        while(left < right) {
            if (s.charAt(left) == s.charAt(right)) {
                left++;
                right--;
            } else {
                return false;
            }
        }

        return true;
    }
}