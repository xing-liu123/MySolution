class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            nums_map = set()
            
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j - 1] == nums[j - 2]:
                    continue
                
                num = -nums[i] - nums[j]
                
                if num in nums_map:
                    res.append([nums[i], num, nums[j]])
                    nums_map.remove(num)
                else:
                    nums_map.add(nums[j])
                
        return res