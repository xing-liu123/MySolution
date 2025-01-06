class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.strip().split()

        left, right = 0, len(str_list) - 1

        while left < right:
            str_list[left], str_list[right] = str_list[right].strip(), str_list[left].strip()
            left += 1
            right -= 1

        return ' '.join(str_list)