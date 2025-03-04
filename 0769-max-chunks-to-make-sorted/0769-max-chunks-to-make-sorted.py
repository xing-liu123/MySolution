class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
 
        currRight = 0
        chunks = 0

        for right in range(n):
            
            currRight = max(currRight, arr[right])
            if currRight == right:
                chunks += 1

        return chunks