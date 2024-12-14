class Trie:
    class Node():
        def __init__(self):
            self.children = [None] * 26
            self.end = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = self.Node()

            curr = curr.children[idx]
        
        curr.end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            
            curr = curr.children[idx]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            
            curr = curr.children[idx]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)