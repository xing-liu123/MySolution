class Solution:
    def maximumLength(self, s: str) -> int:
        # Store counts of consecutive character lengths
        char_lengths = defaultdict(list)
        
        # Count consecutive characters
        curr_count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_count += 1
            else:
                char_lengths[s[i-1]].append(curr_count)
                curr_count = 1
        # Don't forget to add the last sequence
        char_lengths[s[-1]].append(curr_count)
        
        max_len = -1
        
        for lengths in char_lengths.values():
            lengths.sort(reverse=True)
            
            if len(lengths) == 1:
                if lengths[0] >= 3:
                    max_len = max(max_len, lengths[0] - 2)
            elif len(lengths) == 2:
                if lengths[0] <= 1:
                    continue
                first = lengths[0] - 2
                second = min(lengths[0] - 1, lengths[1])

                curr_len = max(first, second)

                if curr_len > 0:
                    max_len = max(max_len, curr_len)

            else:
                first = lengths[0] - 2  # only use the first one
                second = min(lengths[0] - 1, lengths[1]) # use first and second one

                curr_len = max(first, second, lengths[2]) # also use first three

                if curr_len > 0:
                    max_len = max(max_len, curr_len)


        return max_len
