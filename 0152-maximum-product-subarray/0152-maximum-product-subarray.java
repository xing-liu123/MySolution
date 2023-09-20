class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        int currMin = 1;
        int currMax = 1;

        for (int num : nums) {
            int temp = currMax * num;

            currMax = Math.max(currMax * num, Math.max(num, currMin * num));
            currMin = Math.min(temp, Math.min(num, currMin * num));
            res = Math.max(currMax, res);
        }

        return res;
    }
}