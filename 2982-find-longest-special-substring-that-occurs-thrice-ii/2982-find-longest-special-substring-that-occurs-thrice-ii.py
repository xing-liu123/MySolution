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
            
            # Try each possible substring length
            curr_len = lengths[0] if lengths else 0
            while curr_len > 0:
                count = 0
                remaining = lengths.copy()
                
                # Count how many non-overlapping substrings we can form
                for length in remaining:
                    # From a length L, we can form L-curr_len+1 substrings of length curr_len
                    count += max(0, length - curr_len + 1)
                    
                if count >= 3:
                    max_len = max(max_len, curr_len)
                    break
                    
                curr_len -= 1
        
        return max_len
