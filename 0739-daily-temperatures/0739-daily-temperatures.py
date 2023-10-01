class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        stack.append(0)
        res = [0] * n

        for i in range(1, n):
            if (temperatures[i] <= temperatures[stack[-1]]):
                stack.append(i)
            else:
                while (len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]):
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        
        return res
                    
            