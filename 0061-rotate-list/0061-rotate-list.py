# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
            
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        k %= length
        
        if k == 0:
            return head

        fast = head

        while k > 0:
            fast = fast.next
            k -= 1

        slow = head

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head