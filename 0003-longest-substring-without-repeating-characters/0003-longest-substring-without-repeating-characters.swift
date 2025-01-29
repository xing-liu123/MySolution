class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var lastIndex: [Character:Int] = [:]
        var longest = 0
        var left = 0

        for (right, char) in s.enumerated() {

            if let index = lastIndex[char] {
                left = index + 1
            }

            lastIndex[char] = right


            longest = max(longest, right - left + 1)
        }

        return longest
     }
}