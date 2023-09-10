class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int n = intervals.length;

        if (n == 0) {
             int[][] res = new int[1][2];
             res[0] = newInterval;
            return res;
        }

        int left = newInterval[0];
        int right = newInterval[1];

        if (right < intervals[0][0]) {
            int[][] res = new int[n + 1][2];
            res[0] = newInterval;
            copy(res, intervals, 1, n, 0, n - 1);
            return res;
        } else if (right == intervals[0][0] || right <= intervals[0][1]) {
            intervals[0][0] = Math.min(intervals[0][0], left);
            return intervals;
        } else if (left > intervals[n - 1][1]) {
            int[][] res = new int[n + 1][2];
            res[n] = newInterval;
            copy(res, intervals, 0, n - 1, 0, n - 1);
            return res;
        } else if (left == intervals[n - 1][1] || left >= intervals[n - 1][0]) {
            intervals[n - 1][1] = Math.max(intervals[n - 1][1], right);
            return intervals;
        }

        int left_idx = -1;
        int right_idx = -1;

        for (int i = 0; i < n; i++) {
            if (intervals[i][1] >= left) {
                left_idx = i;
                break;
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            if (intervals[i][0] <= right) {
                right_idx = i;
                break;
            }
        }

        int[][] res = new int[n - (right_idx - left_idx)][2];
        res[left_idx][0] = Math.min(intervals[left_idx][0], left); 
        res[left_idx][1] = Math.max(intervals[right_idx][1], right); 
        copy(res, intervals, 0, left_idx - 1, 0, left_idx - 1);
        copy(res, intervals, left_idx + 1, n - (right_idx - left_idx) - 1, right_idx + 1, n - 1);
        return res;
        
    }

    private void copy(int[][] newArr, int[][] orgin, int start1, int end1, int start2, int end2) {
        while (start1 <= end1) {
            newArr[start1++] = orgin[start2++];
        }
    }
}