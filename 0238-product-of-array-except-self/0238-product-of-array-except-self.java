class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] leftPro = new int[nums.length];
        int[] rightPro = new int[nums.length];

        leftPro[0] = 1;

        for (int i = 1; i < nums.length; i++) {
            leftPro[i] = nums[i - 1] * leftPro[i - 1];
        }

        rightPro[nums.length - 1] = 1;

        for (int i = nums.length - 2; i >= 0; i--) {
            rightPro[i] = nums[i + 1] * rightPro[i + 1];
        }

        for (int i = 0; i < nums.length; i++) {
            nums[i] = leftPro[i] * rightPro[i];
        }

        return nums;
    }
}