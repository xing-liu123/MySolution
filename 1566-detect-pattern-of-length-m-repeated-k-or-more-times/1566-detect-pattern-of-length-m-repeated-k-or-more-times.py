class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m * k > len(arr):
            return False

        for i in range(len(arr) - m * k + 1):
            if arr[i: i + m * k] == k * arr[i: i + m]:
                return True

        return False