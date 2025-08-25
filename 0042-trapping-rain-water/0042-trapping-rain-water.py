class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []

        water = 0

        for right in range(len(height)):
            while stack and height[right] > height[stack[-1]]:
                mid = stack.pop()

                if stack:
                    left = stack[-1]
                    h = min(height[left], height[right]) - height[mid]
                    w = right - left - 1
                    water += h * w
            
            stack.append(right)

        return water
