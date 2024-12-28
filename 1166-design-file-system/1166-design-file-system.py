class TrieNode:
    def __init__(self, name: str, val: int):
        self.children = {}
        self.name = name
        self.val = val

class FileSystem:
    
    def __init__(self):
        self.root = TrieNode("", -1)

    def createPath(self, path: str, value: int) -> bool:
        curr = self.root
        node = path.split("/")[1:]
        curr_idx = 0

        while curr_idx < len(node) and node[curr_idx] in curr.children:
            curr = curr.children[node[curr_idx]]
            curr_idx += 1
        
        if curr_idx != len(node) - 1:
            return False
        
        curr.children[node[curr_idx]] = TrieNode(node[-1], value)
        return True

    def get(self, path: str) -> int:
        curr = self.root
        node = path.split("/")[1:]
        curr_idx = 0

        while curr_idx < len(node) and node[curr_idx] in curr.children:
            curr = curr.children[node[curr_idx]]
            curr_idx += 1
        
        if curr_idx != len(node):
            return -1

        return curr.val



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)