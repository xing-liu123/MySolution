class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        count = 0

        for c in s:
            if c in chars:
                chars.clear()
                count += 1
            chars.add(c)

        return count + 1
