class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneCount = 0

        for d in data:
            if d == 1:
                oneCount += 1

        left = 0

        ones, oneMost = 0, 0

        for right in range(len(data)):
            if data[right] == 1:
                ones += 1

            if right - left + 1 > oneCount:
                if data[left] == 1:
                    ones -= 1
                left += 1
            
            oneMost = max(oneMost, ones)

        return oneCount - oneMost
            



            