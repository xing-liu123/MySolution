class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word_counts2 = {}

        for word in words2:
            word_counts2[word] = Counter(word)

        def isUniversal(s1):
            
            count1 = Counter(s1)

            for count in word_counts2.values():
                for char in count.keys():
                    if count1[char] < count[char]:
                        return False

            return True

        res = []
        
        for w1 in words1:
            if isUniversal(w1):
                res.append(w1)

        return res
            