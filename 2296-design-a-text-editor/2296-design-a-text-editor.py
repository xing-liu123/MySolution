class Node:
    def __init__(self, char = None):
        self.char = char
        self.next = None
        self.prev = None

class TextEditor:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.head
        

    def addText(self, text: str) -> None:
        for c in text:
            node = Node(c)
            node.prev = self.cursor
            node.next = self.cursor.next
            self.cursor.next.prev = node
            self.cursor.next = node
            self.cursor = node

    def deleteText(self, k: int) -> int:
        count = 0

        while self.cursor != self.head and count < k:
            prev = self.cursor.prev
            prev.next = self.cursor.next
            self.cursor.next.prev = prev
            self.cursor = prev
            count += 1
        
        return count
        
    def cursorLeft(self, k: int) -> str:
        for _ in range(k):
            if self.cursor == self.head:
                break
            self.cursor = self.cursor.prev

        return self.getTenChars()
        

    def cursorRight(self, k: int) -> str:
        for _ in range(k):
            if self.cursor.next == self.tail:
                break
            self.cursor = self.cursor.next

        return self.getTenChars()

    def getTenChars(self) -> str:
        text = []
        curr = self.cursor

        for i in range(10):
            if curr == self.head:
                break
            text.append(curr.char)

            curr = curr.prev

        return ''.join(reversed(text))


        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)