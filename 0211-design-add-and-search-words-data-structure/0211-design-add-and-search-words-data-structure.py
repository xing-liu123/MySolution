class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if not c in curr.children:
                curr.children[c] = Node()
            
            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, pos):
            if pos == len(word):
                return node.end

            char = word[pos]

            if char == ".":
                return any(dfs(child, pos + 1) for child in node.children.values())
            elif char in node.children:
                return dfs(node.children[char], pos + 1)

            return False

        return dfs(self.root, 0)
        # stack = [(self.root, word)]

        # while stack:
        #     currNode, currWord = stack.pop()

        #     if not currWord:
        #         if currNode.end:
        #             return True
        #         continue
            
        #     if currWord[0] == ".":
        #         for nextNode in currNode.children.values():
        #             stack.append((nextNode, currWord[1:]))
        #     else:
        #         if currWord[0] in currNode.children:
        #             stack.append((currNode.children[currWord[0]], currWord[1:]))

        # return False
        




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)