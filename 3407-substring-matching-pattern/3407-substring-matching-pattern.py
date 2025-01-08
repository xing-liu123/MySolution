class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split("*")

        left_idx = s.find(left)
        right_idx = s.rfind(right)

        if left_idx == -1 or right_idx == -1:
            return False

        return left_idx + len(left) < right_idx