from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []

        wordCount = defaultdict(int)
        wordLength = len(words[0])
        totalLength = wordLength * len(words)

        if len(s) < totalLength:
            return res

        for word in words:
            wordCount[word] += 1

        left = 0
        currWordCount = defaultdict(int)

        def isValid(left, right):
            for i in range(left, right + 1, wordLength):
                currWord = s[i: i + wordLength]
                if not currWord in wordCount:
                    return False
                currWordCount[currWord] += 1
                if currWordCount[currWord] > wordCount[currWord]:
                    return False

            return True

        for right in range(totalLength - 1, len(s)):
            if isValid(left, right):
                res.append(left)
            left += 1
            currWordCount = defaultdict(int)

        return res