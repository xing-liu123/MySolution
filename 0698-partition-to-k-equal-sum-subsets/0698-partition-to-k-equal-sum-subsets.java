class Solution {
    int[] sums;
    int target = 0;

    public boolean canPartitionKSubsets(int[] nums, int k) {
        int totalSum = 0;

        for (int num : nums) {
            totalSum += num;
        }

        if (totalSum % k != 0) {
            return false;
        }

        target = totalSum / k;

        sums = new int[k];
        return backtrack(nums, k, 0);    
    }

    private boolean backtrack(int[] nums, int k, int idx) {
        if (idx == nums.length) {
            return isValid(sums);
        }

        for (int i = 0; i < k; i++) {
            if (sums[i] + nums[idx] > target) {
                continue;
            }

            sums[i] += nums[idx];
            if (backtrack(nums, k, idx + 1)) {
                return true;
            }
            sums[i] -= nums[idx];

            if (sums[i] == 0 || sums[i] + nums[idx] == target) {
                break;
            }
        }

        return false;
    }

    private boolean isValid(int[] sums) {
        for (int sum : sums) {
            if (sum != target) {
                return false;
            }
        }

        return true;
    }
}