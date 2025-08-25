class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def isValid(index):
            count = 0

            for c in citations:
                if c >= index:
                    count += 1

            return count >= index
        
        low, high = 0, len(citations)

        while low <= high:
            mid = (low + high) // 2

            if isValid(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return high