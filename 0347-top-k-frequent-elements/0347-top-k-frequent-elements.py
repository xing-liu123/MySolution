class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}

        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        freq_list = list(num_counts.items())

        def quickSelect(left, right, kLargest):
            if left == right:
                return

            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            if pivot_idx == kLargest:
                return
            elif pivot_idx > kLargest:
                quickSelect(left, pivot_idx - 1, kLargest)
            else:
                quickSelect(pivot_idx + 1, right, kLargest)

        def partition(left, right, pivot_idx):
            pivot_freq = freq_list[pivot_idx][1]

            freq_list[pivot_idx], freq_list[right] = freq_list[right], freq_list[pivot_idx]

            stored_idx = left

            for i in range(left, right):
                if freq_list[i][1] > pivot_freq:
                    freq_list[stored_idx], freq_list[i] = freq_list[i], freq_list[stored_idx]
                    stored_idx += 1

            freq_list[stored_idx], freq_list[right] = freq_list[right], freq_list[stored_idx]

            return stored_idx

            
        n = len(freq_list)

        quickSelect(0, n - 1, k - 1)

        return [num for num, _ in freq_list[:k]]


        # minHeap = [] 

        # for num, count in num_counts.items():
        #     heapq.heappush(minHeap, (count, num))

        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)

        # return [num for _, num in minHeap]