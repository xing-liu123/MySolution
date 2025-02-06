class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0

            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        seen = set([s])
        found = False
        res = []

        while queue:
            size = len(queue)

            for _ in range(size):
                string = queue.popleft()

                if isValid(string):
                    res.append(string)
                    found = True

                if found:
                    continue

                for i in range(len(string)):
                    if string[i].isalpha():
                        continue

                    new_string = string[:i] + string[i + 1:]

                    if not new_string in seen:
                        seen.add(new_string)
                        queue.append(new_string)

            if found:
                break

        return res
