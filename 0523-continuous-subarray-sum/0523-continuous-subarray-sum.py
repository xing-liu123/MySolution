class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        remainder_map = {0: -1}
        currSum = 0

        for i, num in enumerate(nums):

            currSum += num
            r = currSum % k
            
            if r in remainder_map and remainder_map[r] < i - 1:
                return True
            
            if r not in remainder_map:
                remainder_map[r] = i
            

        return False
