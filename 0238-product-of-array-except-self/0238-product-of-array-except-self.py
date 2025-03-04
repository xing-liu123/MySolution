class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeroCount = 0
        product = 1

        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroCount += 1

        if zeroCount > 1:
            return [0] * n
        elif zeroCount == 1:
            return [0 if num != 0 else product for num in nums]

        res = []

        for num in nums:
            res.append(product // num)

        return res

