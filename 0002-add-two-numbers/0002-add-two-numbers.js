/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);
    let curr = dummy;
    let carry = 0;
    
    while (l1 != null || l2 != null || carry != 0) {
        let val1 = (l1 == null) ? 0 : l1.val;
        let val2 = (l2 == null) ? 0 : l2.val;
        
        let sum = val1 + val2 + carry;
        carry = Math.floor(sum / 10);
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        
        if (l1 != null) {
            l1 = l1.next;
        }
        
        if (l2 != null) {
            l2 = l2.next;
        }
         
        
    }
    
    return dummy.next;
};