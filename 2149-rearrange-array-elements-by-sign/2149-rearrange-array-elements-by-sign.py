class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        pos, neg = 0, 0

        for i in range(0, n, 2):
            while pos < n and nums[pos] <= 0:
                pos += 1

            res[i] = nums[pos]
            pos += 1
            while neg < n and nums[neg] >= 0:
                neg += 1
            
            res[i + 1] = nums[neg]
            neg += 1

        return res
            

            




