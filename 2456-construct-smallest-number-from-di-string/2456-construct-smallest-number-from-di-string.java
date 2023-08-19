class Solution {
    char[] res;
    int[] used = new int[9];
    public String smallestNumber(String pattern) {
        res = new char[pattern.length() + 1];
        char[] pat = pattern.toCharArray();
        backtracking(pat, 0);
        return new String(res);
    
    }

    private boolean backtracking(char[] pattern, int idx) {
        if (idx == pattern.length + 1) {
            return true;
        }

        for (char c = '1'; c <= '9'; c++) {
            if (used[c - '1'] == 0) {
                if (idx == 0 || (pattern[idx - 1] == 'I' && c > res[idx - 1]) || (pattern[idx - 1] == 'D' && c < res[idx - 1])) {
                    used[c - '1'] = 1;
                    res[idx] = c;
                    if(backtracking(pattern, idx + 1)) {
                        return true;
                    }
                    used[c - '1'] = 0;
                    res[idx] = ' ';
                }
            }
        }
        return false;
    }

  
}