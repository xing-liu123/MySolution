class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) <= 2:
        #     return len(nums)

        left = 1

        for right in range(2, len(nums)):
            if not (nums[left - 1] == nums[left] and nums[left] == nums[right]):
                left += 1
                nums[left] = nums[right]
        
        return left + 1