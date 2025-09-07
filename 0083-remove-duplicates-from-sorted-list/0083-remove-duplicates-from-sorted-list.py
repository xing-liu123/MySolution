# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        left = head
        right = head

        while right:
            if right.val == left.val:
                right = right.next
            else:
                left.next = right
                left = right
                right = right.next

        left.next = None
        
        return head