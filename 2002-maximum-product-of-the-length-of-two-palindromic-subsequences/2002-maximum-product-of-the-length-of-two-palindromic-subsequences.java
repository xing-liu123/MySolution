class Solution {
    int maxProduct = 0;
    public int maxProduct(String s) {
        backtrack(s, 0, "", "");
        return maxProduct;
    }

    private void backtrack(String s, int idx, String sub1, String sub2) {
        if (idx == s.length()) {
            if (isPalindrom(sub1) && isPalindrom(sub2)) {
                maxProduct = Math.max(maxProduct, sub1.length() * sub2.length());
            }   
            return;
        }

        backtrack(s, idx + 1, sub1 + s.charAt(idx), sub2);
        backtrack(s, idx + 1, sub1, sub2 + s.charAt(idx));
        backtrack(s, idx + 1, sub1, sub2);
    }





    private boolean isPalindrom(String s) {
        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}