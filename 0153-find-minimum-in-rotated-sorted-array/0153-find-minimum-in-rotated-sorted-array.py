class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] <= nums[right]:
                return nums[left]
            elif nums[right] < nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[mid] <= nums[right] < nums[left]:
                right = mid - 1

        return -1
