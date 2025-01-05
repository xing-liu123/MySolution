class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1
        
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if nums[right] >= nums[mid]:
                    right = mid - 1
                else:
                    if nums[left] <= target:
                        right = mid - 1
                    else:
                        left = mid + 1
                
            elif target > nums[mid]:
                if nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    if nums[right] >= target:
                        left = mid + 1
                    else:
                        right = mid - 1
                    
        
        return -1