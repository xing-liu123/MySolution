class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
 
        currRight = 0
        chunks = 0

        for right in range(n):
            if right > currRight:
                chunks += 1
            currRight = max(currRight, arr[right])

        return chunks + 1