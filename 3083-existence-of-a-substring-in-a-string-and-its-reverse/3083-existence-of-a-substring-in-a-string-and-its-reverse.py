class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversedSubstrs = set()

        for i in range(1, len(s)):
            reversedSubstr = s[i] + s[i - 1]
            reversedSubstrs.add(reversedSubstr)

        for i in range(1, len(s)):
            substr = s[i - 1] + s[i]

            if substr in reversedSubstrs:
                return True


        return False

            
