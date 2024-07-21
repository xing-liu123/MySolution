class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        new_nums = nums + nums

        stack = [0]

        for i in range(1, len(new_nums)):
            if new_nums[i] <= nums[stack[-1]]:
                stack.append(i % len(nums))
            else:
                while stack and new_nums[i] > nums[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = new_nums[i]
                
                stack.append(i % len(nums))
        
        return res
