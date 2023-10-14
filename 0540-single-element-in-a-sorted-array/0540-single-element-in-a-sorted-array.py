class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mask = 0

        for num in nums:
            mask ^= num
        
        return mask