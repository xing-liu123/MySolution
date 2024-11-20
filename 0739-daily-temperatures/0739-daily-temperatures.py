class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        n = len(temperatures)
        res = [0] * n

        for i in range(1, n):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    idx = stack.pop()
                    res[idx] = i - idx

                stack.append(i)

        return res
        
        