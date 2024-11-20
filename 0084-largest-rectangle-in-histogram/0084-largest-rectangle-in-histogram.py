class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        print(heights)
        stack = [0]
        res = 0

        for i in range(1, len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    idx = stack.pop()
                    h = heights[idx]
                    res = max(res, (i - stack[-1] - 1) * h)

                stack.append(i)

        return res