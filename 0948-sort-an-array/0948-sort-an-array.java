class Solution {
    public int[] sortArray(int[] nums) {
        int[] res = new int[nums.length];
        mergesort(nums, 0, nums.length - 1, res);
        return res;
    }

    private void mergesort(int[] nums, int start, int end, int[] res) {
        if (end - start < 1) {
            return;
        }
        int mid = start + (end - start) / 2;
        if ((end - start) % 2 == 1) {
            mid++;
        }
        mergesort(nums, start, mid - 1, res);
        mergesort(nums, mid, end, res);
        merge(nums, start, mid, end, res);
    }

    private void merge(int[] nums, int start, int mid, int end, int[] res) {
        int idx = 0, i = start, j = mid;

        while (i < mid && j <= end) {
            while (i < mid && nums[i] <= nums[j]) {
                res[idx++] = nums[i++];
            }

            while (j <= end && nums[j] <= nums[i]) {
                res[idx++] = nums[j++];
            }
        }

        while (i < mid) {
            res[idx++] = nums[i++];
        }

        while (j <= end) {
            res[idx++] = nums[j++];
        }

        for (int k = 0; k < idx; k++) {
            nums[start + k] = res[k];
        }

        
    }
}