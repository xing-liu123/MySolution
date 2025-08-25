class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not (s[left].isalpha() or s[left].isdigit()):
                left += 1
            
            while right > left and not (s[right].isalpha() or s[right].isdigit()):
                right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True