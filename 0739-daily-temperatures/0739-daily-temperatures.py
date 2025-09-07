class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        results = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                day = stack.pop()
                results[day] = i - day
            stack.append(i)

        return results
        