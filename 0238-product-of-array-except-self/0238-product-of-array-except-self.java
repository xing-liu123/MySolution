class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];

        answer[0] = 1;

        for (int i = 1; i < answer.length; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }

       
        int rightPro = 1;
        for (int i = answer.length - 1; i >= 0; i--) {
            answer[i] = answer[i] * rightPro;
            rightPro *= nums[i];
        }

        return answer;
    }
}