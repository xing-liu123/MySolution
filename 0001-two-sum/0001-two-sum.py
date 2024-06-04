class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums_map = {}
        
        for index, num in enumerate(nums):
            if target - num in nums_map:
                res.append(index)
                res.append(nums_map[target - num])
                return res
            
            nums_map[num] = index
        
        return res