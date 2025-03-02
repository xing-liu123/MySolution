class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return 0
        
        leftChar = s[0]
        rightChar = s[-1]

        if leftChar == rightChar:
            return self.minMovesToMakePalindrome(s[1:-1])

        idxLeft = s.find(rightChar)
        idxRight = s.rfind(leftChar)

        if idxLeft <= len(s) - idxRight - 1:
            return idxLeft + self.minMovesToMakePalindrome(s[:idxLeft] + s[idxLeft + 1: -1])
        else:
            return len(s) - idxRight - 1 + self.minMovesToMakePalindrome(s[1:idxRight] + s[idxRight + 1:])