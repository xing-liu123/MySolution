class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights.append(0)
        heights.insert(0, 0)

        stack = [0]

        for i in range(1, len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
            else:

                while stack and heights[i] < heights[stack[-1]]:
                   mid = stack.pop()

                   if stack:
                        left = stack[-1]
                        h = heights[mid]
                        w = i - left - 1
                        a = h * w
                        res = max(res, a)
                stack.append(i)
        
        return res

