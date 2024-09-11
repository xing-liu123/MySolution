class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneCount = sum(data)

        left = 0

        curr_sum, max_sum = 0, 0

        for right in range(len(data)):
            curr_sum += data[right]

            if right - left + 1 > oneCount:
                curr_sum -= data[left]
                left += 1
            
            max_sum = max(max_sum, curr_sum)

        return oneCount - max_sum
            



            