class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return n
        
        prevDiff = 0
        currDiff = 0
        count = 1

        for i in range(n - 1):
            currDiff = nums[i + 1] - nums[i]

            if currDiff > 0 and prevDiff <= 0 or currDiff < 0 and prevDiff >= 0:
                count += 1
                prevDiff = currDiff

        return count