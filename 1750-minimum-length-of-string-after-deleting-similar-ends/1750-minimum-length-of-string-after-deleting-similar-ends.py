class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                c = s[left]
                while left <= right and s[left] == c:
                    left += 1

                while left <= right and s[right] == c: 
                    right -= 1
            else:
                break
        
        return right - left + 1