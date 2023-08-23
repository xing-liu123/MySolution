class Solution {
    public int minimizeMax(int[] nums, int p) {
        Arrays.sort(nums);

        int left = 0, right = nums[nums.length - 1] - nums[0];
        while (left <= right) {
            int mid = (left + right) / 2;

            if (can_form(nums, mid, p)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean can_form(int[] nums, int mid, int p) {
        int count = 0;
        for (int i = 0; i < nums.length - 1 && count < p;) {
            if (nums[i + 1] - nums[i] <= mid) {
                i+=2;
                count++;
            } else {
                i++;
            }
        }
        return count >= p;
    }
}