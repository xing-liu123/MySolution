class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        counts = [[0, 0] for _ in range(n)] #max, min

        maxStack = []
        minStack = []

        for i in range(n):
            while maxStack and nums[i] >= nums[maxStack[-1]]:
                maxStack.pop()

            maxLeft = maxStack[-1] + 1 if maxStack else 0
            maxStack.append(i)
            counts[i][0] = i - maxLeft + 1

            while minStack and nums[i] <= nums[minStack[-1]]:
                minStack.pop()

            minLeft = minStack[-1] + 1 if minStack else 0
            minStack.append(i)
            counts[i][1] = i - minLeft + 1

        maxStack = []
        minStack = []

        for i in range(n - 1, -1, -1):
            while maxStack and nums[i] > nums[maxStack[-1]]:
                maxStack.pop()

            maxRight = maxStack[-1] - 1 if maxStack else n - 1
            maxStack.append(i)
            counts[i][0] *= maxRight - i + 1

            while minStack and nums[i] < nums[minStack[-1]]:
                minStack.pop()

            minRight = minStack[-1] - 1 if minStack else n - 1
            minStack.append(i)
            counts[i][1] *= minRight - i + 1

        res = 0
        for i in range(n):
            maxCount, minCount = counts[i]

            res += (maxCount - minCount) * nums[i]

        return res
            
