class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0

        idx1 = len(a) - 1
        idx2 = len(b) - 1
        res = []

        while idx1 >= 0 or idx2 >= 0:
            if idx1 < 0:
                if b[idx2] == "0":
                    if carry == 1:
                        res.append("1")
                        carry = 0
                    else:
                        res.append("0")
                else:
                    if carry == 1:
                        res.append("0")
                        carry = 1
                    else:
                        res.append("1")
                
                idx2 -= 1

            elif idx2 < 0:
                if a[idx1] == "0":
                    if carry == 1:
                        res.append("1")
                        carry = 0
                    else:
                        res.append("0")
                else:
                    if carry == 1:
                        res.append("0")
                        carry = 1
                    else:
                        res.append("1")
                
                idx1 -= 1
            else:
                if a[idx1] == "0" and b[idx2] == "0":
                    if carry == 1:
                        res.append("1")
                        carry = 0
                    else:
                        res.append("0")
                elif a[idx1] == "1" and b[idx2] == "1":
                    if carry == 1:
                        res.append("1")
                    else:
                        res.append("0")
                        carry = 1
                else:
                    if carry == 1:
                        res.append("0")
                    else:
                        res.append("1")

                idx1 -= 1
                idx2 -= 1

        if carry == 1:
            res.append("1")

        return "".join(reversed(res))
