from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if len(wordSet) == 0 or not endWord in wordSet:
            return 0

        graph = {}
        chars_to_try = string.ascii_lowercase

        queue = deque([beginWord])
        length = 1

        while queue:
            length += 1
            size = len(queue)

            for _ in range(size):
                word = queue.popleft()

                for i in range(len(word)):
                    for char in chars_to_try:
                        new_word = word[:i] + char + word[i + 1:]

                        if new_word == endWord:
                            return length

                        if new_word in wordSet:
                            wordSet.remove(new_word)
                            queue.append(new_word)

        return 0



            