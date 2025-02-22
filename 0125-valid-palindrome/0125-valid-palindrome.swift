class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let s = s.lowercased()
        var left = s.startIndex
        var right = s.index(before: s.endIndex)

        while left < right {
            while left < right && !s[left].isNumber && !s[left].isLetter {
                left = s.index(after: left)
            }

            while left < right && !(s[right].isNumber || s[right].isLetter) {
                right = s.index(before: right)
            }

            if left >= right {
                return true
            }

            if s[left] != s[right] {
                return false
            }

            left = s.index(after: left)
            right = s.index(before: right)
        }

        return true
    }
}