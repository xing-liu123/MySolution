from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if not endWord in word_set:
            return 0

        alphabet = string.ascii_lowercase

        queue = deque([beginWord])
        length = 1

        
        while queue:
            length += 1
            size = len(queue)
            
            for _ in range(size):
                word = queue.popleft()

                for i in range(len(word)):
                    for c in alphabet:
                        next_word = word[:i] + c + word[i + 1:]

                        if next_word == endWord:
                            return length

                        if next_word in word_set:
                            word_set.remove(next_word)
                            queue.append(next_word)

        return 0
