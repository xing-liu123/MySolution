class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oneCount = nums.count(1)
        n = len(nums)

        left = 0
        currOne = 0
        minSwap = oneCount

        for right in range(n + oneCount - 1):
            if nums[right % n] == 1:
                currOne += 1

            if right - left + 1 > oneCount:
                if nums[left] == 1:
                    currOne -= 1

                left += 1
            
            minSwap = min(minSwap, oneCount - currOne)

        return minSwap