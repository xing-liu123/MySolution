class Solution {
public:

    int findKthLargest(vector<int>& nums, int k) {
        return quickselect(nums, k);
    }

    int quickselect(vector<int>& nums, int k) {
      int pivot = nums[rand() % nums.size()];

      vector<int> left;
      vector<int> mid;
      vector<int> right;

      for (int num : nums) {
        if (num > pivot) {
          left.push_back(num);
        } else if (num < pivot) {
          right.push_back(num);
        } else {
          mid.push_back(num);
        }
      }

      if (k <= left.size()) {
        return quickselect(left, k);
      }

      if (left.size() + mid.size() < k) {
        return quickselect(right, k - left.size() - mid.size());
      }

      return pivot;
    }


};