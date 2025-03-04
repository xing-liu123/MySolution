class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        currRight = 0
        sortedArr = sorted(arr)

        numToIdx = defaultdict(list)
        for idx, num in enumerate(sortedArr):
            numToIdx[num].append(idx)

        chunk = 0
        currRight = 0

        for right in range(len(arr)):
            currRight = max(currRight, numToIdx[arr[right]].pop(0))

            if currRight == right:
                chunk += 1

        return chunk