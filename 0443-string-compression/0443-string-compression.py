class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        n = len(chars)
        idx = 0

        for right in range(n + 1):
            if right == n or chars[right] != chars[left]:
                count = right - left

                if count == 1:
                    chars[idx] = chars[left]
                    left += 1
                    idx += 1
                else:                    
                    chars[idx] = chars[left]
                    idx += 1

                    for j in range(len(str(count))):
                        chars[idx] = str(count)[j]
                        idx += 1

                    left += count


        return idx
        
