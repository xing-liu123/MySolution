import bisect 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            pos = bisect.bisect_left(sub, num)
            if pos < len(sub):
                sub[pos] = num
            else:
                sub.append(num)

        return len(sub)