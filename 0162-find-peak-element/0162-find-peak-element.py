class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid == 0:
                if nums[mid + 1] < nums[mid]:
                    return mid
                else:
                    left = 1
            elif mid == len(nums) - 1:
                if nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    right = mid - 1
            
            elif nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid
            elif nums[mid - 1] >= nums[mid]:
                right = mid - 1
            elif nums[mid + 1] >= nums[mid]:
                left = mid + 1

        return 0