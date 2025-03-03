class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack or a > 0 or a < 0 and stack[-1] < 0:
                stack.append(a)
                continue

            if a < 0:
                while stack and stack[-1] > 0 and stack[-1] + a < 0:
                    stack.pop()

                if stack:
                    if stack[-1] < 0:
                        stack.append(a)
                    elif stack[-1] + a == 0:
                        stack.pop()
                else:
                    stack.append(a)


        return stack
            
                
            