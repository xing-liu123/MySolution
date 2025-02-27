class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      
        # def quickselect(nums: List[int], k: int) -> int:
        #     pivotVal = random.choice(nums)  # randomly select a pivot

        #     left = [num for num in nums if num > pivotVal]
        #     mid = [num for num in nums if num == pivotVal]
        #     right = [num for num in nums if num < pivotVal]

        #     if k <= len(left):
        #         return quickselect(left, k)
            
        #     if k > len(left) + len(mid):
        #         return quickselect(right, k - len(left) - len(mid))
            
        #     return pivotVal
        
        # return quickselect(nums, k)

        def quickSelect(left, right, k):
            if left == right:
                return

            pivotIdx = random.randint(left, right)
            pivotVal = nums[pivotIdx]

            i, j, p = left, left, right

            while j <= p:
                if nums[j] > pivotVal:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] < pivotVal:
                    nums[p], nums[j] = nums[j], nums[p]
                    p -= 1
                else:
                    j += 1

            if k <= i - left:
                quickSelect(left, i - 1, k)
            elif k <= p - left + 1:
                return
            else:
                quickSelect(p + 1, right, k - (p - left + 1))
            
            
            
        # def partition(left, right, pivot):
        #     print(left, right)
        #     pivotVal = nums[pivot]

        #     nums[right], nums[pivot] = nums[pivot], nums[right]

        #     storedIdx = left

        #     for idx in range(left, right):
        #         if nums[idx] > pivotVal:
        #             nums[idx], nums[storedIdx] = nums[storedIdx], nums[idx]
        #             storedIdx += 1

        #     nums[right], nums[storedIdx] = nums[storedIdx], nums[right]

        #     return storedIdx
                

        quickSelect(0, len(nums) - 1, k)

        return nums[k - 1]

