class Solution {
    public int maximalRectangle(char[][] matrix) {
        
        int[] dp = new int[matrix[0].length];
        int max = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                dp[j] = matrix[i][j] == '1' ? dp[j] + 1 : 0;
            }

            max = Math.max(max, getMaxArea(dp));
        }
        return max;
    }

    private int getMaxArea(int[] heights) {
        int[] extended = new int[heights.length + 2];

        for (int i = 0; i < heights.length; i++) {
            extended[i + 1] = heights[i];
        }

        Deque<Integer> myDeque = new ArrayDeque<>();
        myDeque.push(0);
        int res = 0;
        for (int i = 1; i < extended.length; i++) {
            if (extended[i] > extended[myDeque.peekFirst()]) {
                myDeque.push(i);
            } else if (extended[i] == extended[myDeque.peekFirst()]) {
                myDeque.pop();
                myDeque.push(i);
            } else {
                while (extended[i] < extended[myDeque.peekFirst()]) {
                    int mid = myDeque.pop();
                    int left = myDeque.peekFirst();
                    int w = i - left - 1;
                    int h = extended[mid];
                    int v = w * h;
                    res = Math.max(v, res);
                }
                myDeque.push(i);
            }
        }
        return res;
    }
}