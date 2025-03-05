class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict) 
        memo = {} 

        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""]
            
            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    rest_sentences = backtrack(end)  # Recursive call
                    for sentence in rest_sentences:
                        result.append(word + (" " + sentence if sentence else ""))

            memo[start] = result  # Store result in memo
            return result

        return backtrack(0)