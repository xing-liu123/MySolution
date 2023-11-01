class Solution {
    public long maxAlternatingSum(int[] nums) {
        long add = nums[0];
        long sub = 0;

        for (int i = 1; i < nums.length; i++) {
            add = Math.max(add, sub + nums[i]);
            sub = Math.max(sub, add - nums[i]);
        }

        return Math.max(add, sub);
    }
}