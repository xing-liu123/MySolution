class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var numToIdx: [Int:Int] = [:]

        for (idx, val) in nums.enumerated() {
            if let compleIdx = numToIdx[target - val] {
                return [idx, compleIdx]
            } 

            numToIdx[val] = idx
            
        }

        return []
    }
}