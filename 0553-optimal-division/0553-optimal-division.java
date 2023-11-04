class Solution {
    public String optimalDivision(int[] nums) {
        StringBuilder sb = new StringBuilder();;
        if (nums.length == 1) {
            sb.append(nums[0]);
        } else if (nums.length == 2) {
            sb.append(nums[0]).append("/").append(nums[1]);
        } else {
            sb.append(nums[0]).append("/(");
            for (int i = 1; i < nums.length - 1; i++) {
                sb.append(nums[i]).append("/");
            }
            sb.append(nums[nums.length - 1]).append(")"); 
        }

        return sb.toString();
    }
}