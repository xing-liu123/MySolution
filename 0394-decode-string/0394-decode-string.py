class Solution:
    def decodeString(self, s: str) -> str:
        def helper(idx):
            decoded = ""
            num = 0

            while idx < len(s):
                char = s[idx]

                if char.isdigit():
                    num = num * 10 + int(char)
                elif char == '[':
                    idx, innerDecoded = helper(idx + 1)
                    decoded += num * innerDecoded
                    num = 0
                elif char == ']':
                    return idx, decoded
                else:
                    decoded += char
                
                idx += 1
        
            return decoded

        return helper(0)
                