class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0

        for right, num in enumerate(nums):
            if num != val:
                nums[left] = num
                left += 1

        return left