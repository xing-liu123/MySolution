from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        checked_word = set()

        if not endWord in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        

        while queue:
            word, length = queue.popleft()
            checked_word.add(word)

            for i in range(len(word)):
                for j in range(26):
                    next_word = word[:i] + chr(ord('a') + j) + word[i + 1:]

                    if next_word == endWord:
                        return length + 1

                    if not next_word in checked_word and next_word in word_set:
                        queue.append((next_word, length + 1))

        return 0
