class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        res = []

        if len(nums) == 0:
            return res
            
        for right in range(1, len(nums)):
            if nums[right] > nums[right - 1] + 1:
                if left == right - 1:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[right - 1]))
                
                left = right

        if left == len(nums) - 1:
            res.append(str(nums[-1]))
        else:
            res.append(str(nums[left]) + "->" + str(nums[- 1]))

        return res