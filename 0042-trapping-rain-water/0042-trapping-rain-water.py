class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i in range(len(height)):
            if not stack or height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    idx = stack.pop()

                    if stack:
                        left = stack[-1]
                        h = min(height[left], height[i]) - height[idx]
                        w = i - left - 1
                        water += h * w
                
                stack.append(i)

        return water
