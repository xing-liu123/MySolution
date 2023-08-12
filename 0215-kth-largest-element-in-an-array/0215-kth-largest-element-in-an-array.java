class Solution {
    public int findKthLargest(int[] nums, int k) {
       return quickSelect(nums, 0, nums.length - 1, k);
    }

    private int quickSelect(int[] nums, int left, int right, int k) {
      int pivot = partition(nums, left, right);

      if (pivot == k - 1) {
        return nums[pivot];
      }

      if (pivot < k - 1) {
        return quickSelect(nums, pivot + 1, right, k);
      } else {
        return quickSelect(nums, left, pivot - 1, k);
      }
    }

    private int partition(int[] nums, int left, int right) {
      int pivot = nums[right];

      int i = left, j = right - 1;

      while (i <= j) {
        while (i <= j && nums[i] >= pivot) {
          i++;
        }

        while (i <= j && nums[j] <= pivot) {
          j--;
        }

        if (i <= j) {
          swap(nums, i, j);
          i++;
          j--;
        }
      }
      System.out.println(i);
      swap(nums, i, right);
      return i;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

