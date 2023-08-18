class Solution {
    int max = Integer.MAX_VALUE;
    int [] totals;

    public int distributeCookies(int[] cookies, int k) {
        totals = new int[k];
        backtracking(cookies, 0, k);
        return max;
    }

    private void backtracking(int[] cookies, int start, int k) {
        if (start == cookies.length) {
            int maxTotal = maxTotal(totals);
            max = Math.min(max, maxTotal);
            return;
        }

        for (int i = 0; i < k; i++) {
            totals[i] += cookies[start];
            backtracking(cookies, start + 1, k);
            totals[i] -= cookies[start];
        }
    }

    private int maxTotal(int[] totals) {
        int currMax = 0;
        for (int total : totals) {
            if (total > currMax) {
                currMax = total;
            }
        }

        return currMax;
    }
}