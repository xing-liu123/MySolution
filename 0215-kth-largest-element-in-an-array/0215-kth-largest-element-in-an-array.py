from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # def quickSelect(left, right, k):
        #     if left == right:
        #         return

        #     pivotIdx = random.randint(left, right)
        #     pivotVal = nums[pivotIdx]

        #     i, j, p = left, left, right # [left:i] > val, [i:p + 1] == val, [p + 1] < val

        #     while j <= p:
        #         if nums[j] > pivotVal:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #             j += 1
        #         elif nums[j] < pivotVal:
        #             nums[p], nums[j] = nums[j], nums[p]
        #             p -= 1
        #         else:
        #             j += 1

        #     if k <= i - left:
        #         quickSelect(left, i - 1, k)
        #     elif k <= p - left + 1:
        #         return
        #     else:
        #         quickSelect(p + 1, right, k - (p - left + 1))
            
        # quickSelect(0, len(nums) - 1, k)

        # return nums[k - 1]

        minHeap = []

        for num in nums:
            heappush(minHeap, num)

            if len(minHeap) > k:
                heappop(minHeap)

        return minHeap[0]
            
       

        

