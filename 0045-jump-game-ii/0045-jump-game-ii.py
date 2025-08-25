class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        count = 1
        currReach = nums[0]
        currStart = 0

        while currReach < n - 1:
            nextReach = 0

            for i in range(currStart, currReach + 1):
                nextReach = max(nextReach, i + nums[i])

            count += 1
            currStart = currReach + 1
            currReach = nextReach

        return count