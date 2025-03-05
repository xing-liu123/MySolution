class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        
        count = 0

        currProduct = 1

        left = 0

        for right in range(len(nums)):
            currProduct *= nums[right]

            while currProduct >= k:
                currProduct //= nums[left]
                left += 1

            count += (right - left + 1)

        return count