class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # key is the sortedWord
 
        for word in strs:
            charCount = [0] * 26

            for c in word:
                idx = ord(c) - ord('a')
                charCount[idx] += 1
            
            anagrams[tuple(charCount)].append(word)

        return list(anagrams.values())
            

        