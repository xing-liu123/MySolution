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
        def searchFromNode(currWord, currNode):
            if not currWord:
                return currNode.end
            
            c = currWord[0]

            if c == ".":
                for nextNode in currNode.children.values():
                    if searchFromNode(currWord[1:], nextNode):
                        return True
                
                return False

            if not c in currNode.children:
                return False
            else:
                return searchFromNode(currWord[1:], currNode.children[c])
                    
        return searchFromNode(word, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)