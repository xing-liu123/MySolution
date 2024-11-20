class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)

        nums = nums + nums

        stack = [0]

        for i in range(1, len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop() % len(res)
                res[idx] = nums[i]

            stack.append(i)

        return res
