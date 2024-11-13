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
        temp_arr = [0] * len(nums)
        
        # Function to merge two sub-arrays in sorted order.
        def merge(left: int, mid: int, right: int):
            # Calculate the start and sizes of two halves.
            start1 = left
            start2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid

            # Copy elements of both halves into a temporary array.
            for i in range(n1):
                temp_arr[start1 + i] = nums[start1 + i]
            for i in range(n2):
                temp_arr[start2 + i] = nums[start2 + i]

            # Merge the sub-arrays 'in tempArray' back into the original array 'arr' in sorted order.
            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                    nums[k] = temp_arr[start1 + i]
                    i += 1
                else:
                    nums[k] = temp_arr[start2 + j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < n1:
                nums[k] = temp_arr[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp_arr[start2 + j]
                j += 1
                k += 1

        # Recursive function to sort an array using merge sort
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) // 2
            # Sort first and second halves recursively.
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            # Merge the sorted halves.
            merge(left, mid, right)
    
        merge_sort(0, len(nums) - 1)
        return nums