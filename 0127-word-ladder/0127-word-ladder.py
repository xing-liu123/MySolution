from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        visited = set()

        queue = deque([beginWord])
        visited.add(beginWord)
        length = 0

        while queue:
            size = len(queue)
            length += 1
            for _ in range(size):
                word = queue.popleft()

                if word == endWord:
                    return length

                for i in range(len(word)):
                    for j in range(ord('a'), ord('z') + 1):
                        newWord = word[0 : i] + chr(j) + word[i + 1:]

                        if not newWord in visited and newWord in wordSet:
                            visited.add(newWord)
                            queue.append(newWord)

        return 0
                

