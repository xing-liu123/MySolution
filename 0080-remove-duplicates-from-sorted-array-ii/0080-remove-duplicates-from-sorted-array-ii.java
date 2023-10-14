class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;

        if (n <= 2) {
            return n;
        }
        int first = nums[0];
        int second = nums[1];
        int i = 2;
        
        for (int j = 2; j < n; j++) {
            if (first != second || nums[j] != second) {
                nums[i] = nums[j];
                first = nums[i - 1];
                second = nums[i];
                i++;
            }
        }
        return i;
    }
}