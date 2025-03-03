class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)

        res = []

        for word in words:
            if self.dfs(word, 0, 0):
                res.append(word)

        return res
    
    def insert(self, word):
        curr = self.root

        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.isEnd = True
    
    @lru_cache(None)
    def dfs(self, word, idx, count):
        if idx >= len(word):
            return count > 1

        curr = self.root
        for i in range(idx, len(word)):
            p = ord(word[i]) - ord('a')

            if not curr.children[p]:
                return False
            
            curr = curr.children[p]

            if curr.isEnd:
                if self.dfs(word, i + 1, count + 1):
                    return True

        return False

        
