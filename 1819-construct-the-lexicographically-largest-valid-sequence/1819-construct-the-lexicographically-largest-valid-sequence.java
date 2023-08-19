class Solution {
    int[] res;
    int count;
    int[] used;
    public int[] constructDistancedSequence(int n) {
        count = 2 * n - 1;
        used = new int[n + 1];
        res = new int[2 * n - 1];
        backtracking(0, n);
        return res;
    }

    boolean backtracking(int start, int n) {
        if (start == count) {
            return true;
        }

        if (res[start] != 0) {
            return backtracking(start + 1, n);
        } 

        for (int i = used.length - 1; i >= 1; i--) {
           if (used[i] == 0) {
               if (i == 1) {
                 used[i] = 1;
                res[start] = i;
                if (backtracking(start + 1, n)) {
                    return true;
                }
                used[i] = 0;
                res[start] = 0;
               } else if (start + i < count && res[start + i] == 0) {
                   used[i] = 1;
                   res[start] = i;
                   res[start + i] = i;
                   if (backtracking(start + 1, n)) {
                    return true;
                    }
                    used[i] = 0;
                     res[start] = 0;
                   res[start + i] = 0;
               }
           } 
        }

        return false;
    }
}