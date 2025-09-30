class Solution:
    def maximum69Number (self, num: int) -> int:
        strNum = str(num)
        res = ""

        for i in range(len(strNum)):
            if strNum[i] == '6':
                res = strNum[:i] + "9" + strNum[i + 1:]
                break
        
        return int(res) if res != "" else num
            
