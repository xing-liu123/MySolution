from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        maxDeque, minDeque = deque(), deque()

        left = 0

        for right in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()

            maxDeque.append(right)

            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()

            minDeque.append(right)

            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1

                if maxDeque[0] < left:
                    maxDeque.popleft()

                if minDeque[0] < left:
                    minDeque.popleft()

            res = max(res, right - left + 1)

        return res





        # res = 0
        # maxDeque, minDeque = deque(), deque()
        # left = 0

        # for right in range(len(nums)):
        #     while maxDeque and nums[maxDeque[-1]] <= nums[right]:
        #         maxDeque.pop()
        #     maxDeque.append(right)

        #     while minDeque and nums[minDeque[-1]] >= nums[right]:
        #         minDeque.pop()
        #     minDeque.append(right)

        #     while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
        #         left += 1

        #         if maxDeque[0] < left:
        #             maxDeque.popleft()

        #         if minDeque[0] < left:
        #             minDeque.popleft()
            
        #     res = max(res, right - left + 1)

        # return res

            
