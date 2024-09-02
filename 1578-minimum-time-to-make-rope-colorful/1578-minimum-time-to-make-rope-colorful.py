class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        left, right = 0, 1
        count = 0

        while right < n:
            
            if colors[left] != colors[right]:
                left += 1
                right += 1
            else:
                totalTime = neededTime[left] + neededTime[right]
                maxTime = max(neededTime[left], neededTime[right])

                while right + 1 < n and colors[right + 1] == colors[left]:
                    right += 1
                    totalTime += neededTime[right]
                    maxTime = max(maxTime, neededTime[right])
                
                left = right + 1
                right += 2
                count += (totalTime - maxTime)
                    
        return count