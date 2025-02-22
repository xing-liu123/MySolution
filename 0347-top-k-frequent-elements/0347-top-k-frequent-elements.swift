class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var counts: [Int: Int] = [:]

        for num in nums {
            if let count = counts[num] {
                counts[num] = count + 1
            } else {
                counts[num] = 1
            }
        }

        let sortedKeys = counts.keys.sorted{ counts[$0]! > counts[$1]! }

        return Array(sortedKeys.prefix(k))

    }
}