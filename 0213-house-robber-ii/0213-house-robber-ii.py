class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(start, end) -> int:
            if start == end:
                return nums[start]
            x = nums[start]
            y = max(nums[start], nums[start + 1])

            for i in range(start + 2, end + 1):
                z = y
                y = max(x + nums[i], y)
                x = z

            return max(x, y)


        return max(helper(0, n - 2), helper(1, n - 1))