class TrieNode:
    def __init__(self):
        self.children = [None] * 27
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, wordIdx: int):
        for i in range(len(word)):
            subWord = word[i:] + "{" + word
            curr = self.root

            for c in subWord:
                idx = ord(c) - ord('a')
                if not curr.children[idx]:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
                curr.index = wordIdx

    def search(self, word: str):
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return -1
            curr = curr.children[idx]
        
        return curr.index

class WordFilter:

    def __init__(self, words: List[str]):
        self.root = Trie()

        for i in range(len(words)):
            word = words[i]
            self.root.insert(word, i)
        

    def f(self, pref: str, suff: str) -> int:
        return self.root.search(suff + "{" + pref)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)