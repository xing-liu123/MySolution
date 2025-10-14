class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = [0] * n
        currVal = n // 2

        left, right = 0, n - 1

        while left < right:
            arr[left] = currVal
            arr[right] = -currVal
            currVal -= 1
            left += 1
            right -= 1

        return arr