class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * len(s)

        for left, right, direction in shifts:
            diff[left] += direction if direction == 1 else -1
            if right + 1 < len(s):
                diff[right + 1] -= direction if direction == 1 else -1

        chars = list(s)

        curr_sum = 0

        for i, c in enumerate(chars):
            curr_sum += diff[i]
            shift = curr_sum % 26

            curr_ord = ord(chars[i])
            new_char = chr((curr_ord - ord('a') + shift) % 26 + ord('a'))
            chars[i] = new_char

        return ''.join(chars)