class Solution {
    func generateParenthesis(_ n: Int) -> [String] {
        var combination = Array(repeating: "", count: n * 2)
        var res: [String] = []

        func backtracking(_ currIdx: Int, _ openCount: Int, _ closedCount: Int) {
            if currIdx == n * 2 {
                res.append(combination.joined(separator: ""))
                return
            }

            if openCount < n {
                combination[currIdx] = "("
                backtracking(currIdx + 1, openCount + 1, closedCount)
            }

            if closedCount < openCount {
                combination[currIdx] = ")"
                backtracking(currIdx + 1, openCount, closedCount + 1)
            }
        }

        backtracking(0, 0, 0)

        return res
    }
}