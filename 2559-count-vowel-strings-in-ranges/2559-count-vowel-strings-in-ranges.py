class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        ending_in_vowel_counts = [0] * n
        curr_ending_in_vowel_count = 0

        for idx, word in enumerate(words):
            if word[-1] in "aeiou" and word[0] in "aeiou":
                curr_ending_in_vowel_count += 1
            
            ending_in_vowel_counts[idx] = curr_ending_in_vowel_count

        res = []

        for start, end in queries:
            count_end = ending_in_vowel_counts[end]

            count_start =  ending_in_vowel_counts[start - 1] if start > 0 else 0

            res.append(count_end - count_start)

        return res 
            

