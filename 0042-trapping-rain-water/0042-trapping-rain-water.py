class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        stack = [0]

        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] >= height[stack[-1]]:
                    mid = stack.pop()

                    if stack:
                        left = stack[-1]
                        h = min(height[left], height[i]) - height[mid]
                        l = i - left - 1
                        res += h * l
                
                stack.append(i)
                
        
        return res