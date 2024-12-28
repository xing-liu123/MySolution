class TrieNode:
    def __init__(self, name: str, val: int):
        self.children = {}
        self.name = name
        self.val = val

class FileSystem:
    
    def __init__(self):
        self.root = TrieNode("", -1)

    def createPath(self, path: str, value: int) -> bool:
        if path[0] != "/" or path == "/":
            return False

        curr = self.root
        nodes = path.split("/")[1:]

        for i in range(len(nodes) - 1):
            if not nodes[i] in curr.children:
                return False
            
            curr = curr.children[nodes[i]]
        
        if nodes[-1] in curr.children:
            return False
        
        curr.children[nodes[-1]] = TrieNode(nodes[-1], value)

        return True

    def get(self, path: str) -> int:
        curr = self.root
        nodes = path.split("/")[1:]
        curr_idx = 0

        for node in nodes:
            if not node in curr.children:
                return -1
            
            curr = curr.children[node]
        
        return curr.val



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)