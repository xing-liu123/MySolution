class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # insertion
        # n = len(nums)

        # for i in range(1, n):
        #     for j in range(i, -1, -1):
        #         if j > 0 and nums[j - 1] > nums[j]:
        #             nums[j], nums[j - 1] = nums[j - 1], nums[j]
        #         else:
        #             break

        # return nums

        # selection
        
        # for i in range(n):
        #     currMin = i
        #     for j in range(i, n):
        #         if nums[j] < nums[currMin]:
        #             currMin = j

        #     nums[i], nums[currMin] = nums[currMin], nums[i]
        
        # return nums
        arr = [0] * n

        def merge(left, mid, right):
            leftIndex = left
            rightIndex = mid + 1
            index = 0

            while leftIndex <= mid and rightIndex <= right:
        
                while leftIndex <= mid and nums[leftIndex] <= nums[rightIndex]:
                    arr[left + index] = nums[leftIndex]
                    leftIndex += 1
                    index += 1

                while rightIndex <= right and nums[rightIndex] < nums[leftIndex]:
                    arr[left + index] = nums[rightIndex]
                    rightIndex += 1
                    index += 1

            while leftIndex <= mid:
                arr[left + index] = nums[leftIndex]
                leftIndex += 1
                index += 1

            while rightIndex <= right:
                arr[left + index] = nums[rightIndex]
                rightIndex += 1
                index += 1

            for i in range(left, left + index):
                nums[i] = arr[i]
            

        def mergeSort(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid, right)

        mergeSort(0, n - 1)

        return nums