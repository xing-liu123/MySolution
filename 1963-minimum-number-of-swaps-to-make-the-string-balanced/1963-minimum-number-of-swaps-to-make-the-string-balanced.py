class Solution:
    def minSwaps(self, s: str) -> int:
        left, right = 0, len(s) - 1

        leftCount = 0
        rightCount = 0
        count = 0
        while left < right:
            if s[left] == "[":
                leftCount += 1
            else:
                rightCount += 1
            
            if leftCount < rightCount:  
                while left < right and s[right] == "]":
                    right -= 1
                count += 1
                leftCount += 1
                rightCount -= 1
            
            left += 1
        
        return count

