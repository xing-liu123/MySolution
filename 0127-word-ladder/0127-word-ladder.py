from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if not endWord in word_set:
            return 0

        queue = deque([beginWord])

        length = 1

        while queue:
            size = len(queue)
            length += 1

            for _ in range(size):
                word = queue.popleft()

                for i in range(len(word)):
                    for j in range(26):
                        next_word = word[:i] + chr(ord('a') + j) + word[i + 1:]

                        if next_word in word_set:
                            if next_word == endWord:
                                return length

                            queue.append(next_word)
                            word_set.remove(next_word)
            print(queue)
        return 0
                        

            
