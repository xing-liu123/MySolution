class Solution {
    func maxTurbulenceSize(_ arr: [Int]) -> Int {
        if arr.count == 1 {
            return 1
        }

        if arr.count == 2 {
            if arr[0] > arr[1] || arr[0] < arr[1] {
                return 2
            } else {
                return 1
            }
        }

        var currMax: Int
        var left: Int

        if arr[1] > arr[0] || arr[1] < arr[0] {
            currMax = 2
            left = 0
        } else {
            currMax = 1
            left = 1
        }

        for right in 2..<arr.count {
            if arr[right] > arr[right - 1] && arr[right - 1] < arr[right - 2] || arr[right] < arr[right - 1] && arr[right - 1] > arr[right - 2] {
                currMax = max(currMax, right - left + 1)
            } else if arr[right] > arr[right - 1] || arr[right] < arr[right - 1] {
                left = right - 1
                currMax = max(currMax, right - left + 1)
            } else {
                left = right
            }
        }

        return currMax
    }
}