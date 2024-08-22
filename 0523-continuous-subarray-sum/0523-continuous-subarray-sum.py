class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        preSums = [nums[0]]
        remainder_map = {}
        remainder_map[nums[0] % k] = 0

        for i in range(1, len(nums)):
            if nums[i] == 0 and nums[i - 1] == 0:
                return True

            preSums.append(preSums[-1] + nums[i])
            r = preSums[-1] % k
            if r == 0:
                return True
            
            if r in remainder_map and remainder_map[r] < i - 1:
                return True
            
            if r not in remainder_map:
                remainder_map[r] = i
            

        return False
