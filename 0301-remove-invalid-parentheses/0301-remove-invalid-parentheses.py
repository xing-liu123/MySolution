class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            """Helper function to check if a string has balanced parentheses."""
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0  # Valid if all open '(' are closed

        queue = deque([s])  # BFS queue
        visited = set([s])  # Avoid duplicates
        found = False  # Flag to stop BFS when valid strings are found
        result = []

        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if is_valid(curr):
                    result.append(curr)
                    found = True  # Once we find valid strings, we don’t process further deletions
                
                if found:
                    continue  # Stop processing more levels

                for i in range(len(curr)):
                    if curr[i].isalpha():  # Skip non-parentheses characters
                        continue

                    new_str = curr[:i] + curr[i + 1:]  # Remove character at index i
                    
                    if new_str not in visited:
                        queue.append(new_str)
                        visited.add(new_str)
            
            if found:
                break  # Stop BFS when we find the first valid set

        return result
        