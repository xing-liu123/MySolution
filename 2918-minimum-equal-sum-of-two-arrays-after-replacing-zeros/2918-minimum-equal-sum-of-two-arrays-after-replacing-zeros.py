class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        zeroCount1 = 0
        zeroCount2 = 0

        for num in nums1:
            if num == 0:
                zeroCount1 += 1
            sum1 += num
        
        for num in nums2:
            if num == 0:
                zeroCount2 += 1
            sum2 += num

        if zeroCount1 == 0 and zeroCount2 == 0:
            if sum1 == sum2:
                return sum1
            else:
                return -1
        elif zeroCount1 == 0:
            if sum2 + zeroCount2 <= sum1:
                return sum1
            else:
                return -1
        elif zeroCount2 == 0:
            if sum1 + zeroCount1 <= sum2:
                return sum2
            else:
                return -1
        else:
            return max(sum1 + zeroCount1, sum2 + zeroCount2)

