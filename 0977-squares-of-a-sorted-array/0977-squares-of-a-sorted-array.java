class Solution {
    public int[] sortedSquares(int[] nums) {
        int left = 0, right = nums.length - 1, current = nums.length - 1;
        int[] newArray = new int[nums.length];
        while (left <= right) {
            if (Math.abs(nums[right]) >= Math.abs(nums[left])) {
                newArray[current--] = nums[right] * nums[right];
                right--;
            } else {
                newArray[current--] = nums[left] * nums[left];
                left++;

            }
        }
        return newArray;
    }
}