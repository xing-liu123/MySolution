class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for c in word:
            if not c in node.children:
                node.children[c] = TrieNode()
            
            node = node.children[c]

            if len(node.suggestions) < 3:
                node.suggestions.append(word)

    def search(self, word):
        node = self.root
        res = []

        for c in word:
            if c in node.children:
                node = node.children[c]

                res.append(node.suggestions)
            else:
                break

        for _ in range(len(word) - len(res)):
            res.append([])

        return res



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)

        return trie.search(searchWord)