class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # zeroCountIdx = {}
        # zeroCountIdx[0] = -1
        # zeroCount = 0
        # maxLength = 0

        # for idx, num in enumerate(nums):
        #     if num == 0:
        #         zeroCount += 1

        #     left = max(0, zeroCount - k)

        #     if left in zeroCountIdx:
        #         maxLength = max(maxLength, idx - zeroCountIdx[left])

        #     if not zeroCount in zeroCountIdx:
        #         zeroCountIdx[zeroCount] = idx

        # return maxLength
        zeroCount = 0
        left = 0

        maxLength = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength