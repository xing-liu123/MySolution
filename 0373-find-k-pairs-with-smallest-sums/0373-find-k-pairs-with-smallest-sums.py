class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        min_heap = []
        res = []

        # Start with the smallest sum pairs (nums1[i], nums2[0])
        for i in range(min(k, len(nums1))):  # Only push at most k elements to avoid unnecessary work
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(res) < k:
            _, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            # If there's a next element in nums2, push the new pair (nums1[i], nums2[j+1])
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
            

