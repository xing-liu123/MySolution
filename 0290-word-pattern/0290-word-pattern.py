class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        word_char_map = {}
        char_used = set()

        for i in range(len(words)):
            if not words[i] in word_char_map:
                if not pattern[i] in char_used:
                    word_char_map[words[i]] = pattern[i]
                    char_used.add(pattern[i])
                else:
                    return False
            elif word_char_map[words[i]] != pattern[i]:
                return False

        return True
            

        