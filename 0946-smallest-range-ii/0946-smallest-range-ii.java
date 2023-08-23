class Solution {
    public int smallestRangeII(int[] nums, int k) {
        int n = nums.length;

        Arrays.sort(nums);
        int res = nums[n - 1] - nums[0];
        int min = nums[0];
        int max = nums[n - 1];
        for (int i = 0; i < n - 1; i++) {
            int possibleMax = Math.max(nums[i] + k, max - k);
            int possibleMin = Math.min(nums[i + 1] - k, min + k);
            res = Math.min(res, possibleMax - possibleMin);
        }

        return res;
 
    }
}