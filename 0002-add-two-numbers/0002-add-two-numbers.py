# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry > 0:
            if not l1 and not l2:
                curr.next = ListNode(carry)
                break
            elif not l1:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
                currSum = curr.val + carry
                carry = currSum // 10
                curr.val = currSum % 10
            elif not l2:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                currSum = curr.val + carry
                carry = currSum // 10
                curr.val = currSum % 10
            else:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                currSum = curr.val + carry + l2.val
                l2 = l2.next
                carry = currSum // 10
                curr.val = currSum % 10

        return dummy.next








            