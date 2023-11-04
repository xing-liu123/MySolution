class Solution {
    public String optimalDivision(int[] nums) {
        String res = "";
        if (nums.length == 1) {
            res += nums[0];
        } else if (nums.length == 2) {
            res += nums[0] + "/" + nums[1];
        } else {
            res += nums[0] + "/" + "(";
            for (int i = 1; i < nums.length - 1; i++) {
                res += nums[i] + "/";
            }
            res += nums[nums.length - 1] + ")";
        }

        return res;
    }
}