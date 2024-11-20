class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(height)):
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                continue
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                    h = min(height[left], height[i]) - height[mid]
                    w = i - left - 1
                    res += h * w
            
            stack.append(i)
   

        return res

