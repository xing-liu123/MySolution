from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        ends = set(deadends)

        if "0000" in ends and "0000" != target:
            return -1

        steps = 0
        queue = deque(["0000"])
        visited = set()
        visited.add("0000")

        def get_next(num: str, idx: int, increment: bool) -> str:
            digit = int(num[idx])
            
            if increment:
                if digit == 9:
                    digit = 0
                else:
                    digit += 1
            else:
                if digit == 0:
                    digit = 9
                else:
                    digit -= 1
            
            return num[:idx] + str(digit) + num[idx + 1:]


        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()

                if curr == target:
                    return steps

                for i in range(8):
                    next_num = get_next(curr, i % 4, i >= 4)
                    if not next_num in ends and not next_num in visited:
                        queue.append(next_num)
                        visited.add(next_num)
            steps += 1

        return -1



