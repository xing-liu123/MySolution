class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lastSeen = {}

        for idx, num in enumerate(nums):
            if target - num in lastSeen:
                return [idx, lastSeen[target - num]]
            else:
                lastSeen[num] = idx
        
        return
