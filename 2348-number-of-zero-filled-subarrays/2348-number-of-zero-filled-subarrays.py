class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0

        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                if count > 0:
                    res += count * (count + 1) // 2
                    count = 0
        
        res += count * (count + 1) // 2

        return res
