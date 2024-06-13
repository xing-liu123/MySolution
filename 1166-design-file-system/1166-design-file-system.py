class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, path: list[str], val: int) -> bool:
        node = self.root
        
        for i, p in enumerate(path):
            if p not in node.children:
                if i == len(path) - 1:
                    node.children[path[i]] = TrieNode()
                else:
                    return False
                
            node = node.children[p]
        
        if node.val != -1:
            return False
        
        node.val = val
        
        return True
    
    def search(self, path: list[str]) -> int:
        node = self.root
        
        for p in path:
            if p in node.children:
                node = node.children[p]
            else:
                return -1
        
        return node.val       

class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        arr = path.split('/')
        return self.trie.insert([p for p in arr if p], value)

    def get(self, path: str) -> int:
        arr = path.split('/')
        return self.trie.search([p for p in arr if p])


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)