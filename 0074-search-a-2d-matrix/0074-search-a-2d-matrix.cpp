class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left = 0;
        int right = matrix.size() * matrix[0].size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int col = mid % (matrix[0].size());
            int row = mid / (matrix[0].size());

            int val = matrix[row][col];

            if (val > target) {
                right = mid - 1;
            } else if (val < target) {
                left = mid + 1;
            } else {
                return true;
            }
            
        }

        return false;
    }
};