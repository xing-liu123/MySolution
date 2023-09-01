class Solution {
    public int[] productExceptSelf(int[] nums) {
        int sum = 1;
        

        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                sum *= nums[i];
            } else {
                count++;
            }  
        }

        if (count == 0) {
            for (int i = 0; i < nums.length; i++) {
                nums[i] = sum / nums[i];
            }  
        } else if (count == 1) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] == 0) {
                    nums[i] = sum;
                } else {
                    nums[i] = 0;
                }
                
            }  
        } else {
            for (int i = 0; i < nums.length; i++) {
                
                nums[i] = 0;
                
                
            }  
        }

        return nums;
    }
}