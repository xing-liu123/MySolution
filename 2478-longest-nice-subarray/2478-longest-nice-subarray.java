class Solution {
    public int longestNiceSubarray(int[] nums) {
        int n = nums.length;
    int res = 1;

    int left = 0;
    int right = 0;
    while (right < n) {
        boolean isValid = true;
        for (int i = left; i < right; i++) {
            if ((nums[i] & nums[right]) != 0) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            res = Math.max(res, right - left + 1);
            right++;
        } else {
            left++;
            right = left;
        }
    }
    return res;
    }
}