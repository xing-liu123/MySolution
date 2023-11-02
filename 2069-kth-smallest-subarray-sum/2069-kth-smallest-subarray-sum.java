class Solution {
    public int kthSmallestSubarraySum(int[] nums, int k) {
        int left = nums[0];;
        int right = 0;

        for (int num : nums) {
            right += num;
            left = Math.min(left, num);
        }

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (countSubarrays(nums, mid) < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }

           
        }

         return left;
    }

    private int countSubarrays(int[] nums, int target) {
        int n = nums.length;
        int count = 0;
        int left = 0;
        int sum = 0;

        for (int right = 0; right < n; right++) {
            sum += nums[right];

            while (sum > target) {
                sum -= nums[left++];
            }
            count += right - left + 1;
        } 

        return count;
    }
}