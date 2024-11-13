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
        # arr = [0] * n

        # def merge(left, mid, right):
        #     leftIndex = left
        #     rightIndex = mid + 1
        #     index = 0

        #     for i in range(left, right + 1):
        #         arr[i] = nums[i]

        #     while leftIndex <= mid and rightIndex <= right:
        
        #         while leftIndex <= mid and arr[leftIndex] <= arr[rightIndex]:
        #             nums[left + index] = arr[leftIndex]
        #             leftIndex += 1
        #             index += 1

        #         while rightIndex <= right and arr[rightIndex] < arr[leftIndex]:
        #             nums[left + index] = arr[rightIndex]
        #             rightIndex += 1
        #             index += 1

        #     while leftIndex <= mid:
        #         nums[left + index] = arr[leftIndex]
        #         leftIndex += 1
        #         index += 1

        #     while rightIndex <= right:
        #         nums[left + index] = arr[rightIndex]
        #         rightIndex += 1
        #         index += 1
            
        # def mergeSort(left, right):
        #     if right - left < 10:
        #         for i in range(left + 1, right + 1):
        #             j = i
        #             while j > 0 and nums[j] > nums[j - 1]:
        #                 nums[j], nums[j - 1] = nums[j - 1], nums[j]


        #     if left < right:
                
        #         mid = (left + right) // 2
        #         mergeSort(left, mid)
        #         mergeSort(mid + 1, right)
        #         merge(left, mid, right)

        # mergeSort(0, n - 1)

        # return nums
        def quicksort(left, right):
            if left < right:
                pivotVal = nums[(left + right) // 2]
                i, j = left,right

                while i <= j:
                    while nums[i] < pivotVal:
                        i += 1

                    while nums[j] > pivotVal:
                        j -= 1

                    if i <= j:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j -= 1

                quicksort(left, j)
                quicksort(i, right) 

        quicksort(0, n - 1)

        return nums
