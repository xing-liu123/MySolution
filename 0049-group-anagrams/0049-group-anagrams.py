class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # key is the sortedWord
 
        for word in strs:
            sortedWord = str(sorted(word))
            
            anagrams[sortedWord].append(word)

        return list(anagrams.values())
            

        