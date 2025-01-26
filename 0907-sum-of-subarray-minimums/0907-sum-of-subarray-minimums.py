
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        MOD = 10**9 + 7

        stack = []
        PLE = [-1] * n

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                PLE[i] = stack[-1]

            stack.append(i)

        stack = []
        NLE = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                NLE[i] = stack[-1]

            stack.append(i)

        for i in range(n):
            left_count = i - PLE[i]
            right_count = NLE[i] - i

            res += arr[i] * left_count * right_count
            res %= MOD

        return res
        