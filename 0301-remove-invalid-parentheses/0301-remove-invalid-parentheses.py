class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack = []
        remove_count = 0

        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if not stack:
                    remove_count += 1
                else:
                    stack.pop()

        expected_length = len(s) - remove_count - len(stack)

        res = set()
        curr = []

        def backtrack(left, right, idx1, idx2):
            if idx1 == expected_length:
                res.add(''.join(curr))
                return

            for i in range(idx2, len(s)):
                if s[i] == "(":
                    curr.append("(")
                    backtrack(left + 1, right, idx1 + 1, i + 1)
                    curr.pop()
                elif s[i] == ")":
                    if right < left:
                        curr.append(")")
                        backtrack(left, right + 1, idx1 + 1, i + 1)
                        curr.pop()
                else:
                    curr.append(s[i])
                    backtrack(left, right, idx1 + 1, i + 1)
                    curr.pop()

        backtrack(0, 0, 0, 0)

        return list(res)
        