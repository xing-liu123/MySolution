class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        count = 1
        currReach = nums[0]
        currStart = 1

        while currReach < n - 1:
            nextReach = currReach

            for i in range(currStart, currReach + 1):
                nextReach = max(nextReach, i + nums[i])

            currStart = currReach + 1
            currReach = nextReach
            count += 1

        return count

