/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var l1 = l1
        var l2 = l2
        let dummy = ListNode(-1)
        var curr = dummy
        var carry = 0

        while l1 != nil || l2 != nil || carry != 0 {
            let val1 = l1?.val ?? 0
            let val2 = l2?.val ?? 0
            let currSum = val1 + val2 + carry
            carry = currSum / 10
            let currVal = currSum % 10

            curr.next = ListNode(currVal)
            curr = curr.next!
 
            l1 = l1?.next
        
            l2 = l2?.next
        }

        return dummy.next
    }
}