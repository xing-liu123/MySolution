class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = None

        for idx, num in enumerate(nums):
            if idx != num:
                if res == None:
                    res = num
                else:
                    res &= num

        return res if res else 0