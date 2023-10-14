class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        int maxSum = findMax(nums);
        int minSum = findMin(nums);
        return sum == minSum ? maxSum : Math.max(maxSum, sum - minSum);
    }

    private int findMax(int[] nums) {
        int currSum = nums[0];
        int max = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currSum = Math.max(currSum + nums[i], nums[i]);
            max = Math.max(currSum, max);
        }

        return max;
    }   

    private int findMin(int[] nums) {
        int currSum = nums[0];
        int min = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currSum = Math.min(currSum + nums[i], nums[i]);
            min = Math.min(currSum, min);
        }

        return min;
    }
}