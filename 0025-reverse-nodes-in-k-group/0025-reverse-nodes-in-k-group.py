# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        if count < k:
            return head

        prev = None
        curr = head

        for _ in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        head.next = self.reverseKGroup(curr, k)
        return prev

        # if not head:
        #     return None
    
        # curr = head
        # count = 0

        # while count < k and curr:
        #     curr = curr.next
        #     count += 1

        # if count < k:
        #     return head

        # prev = None
        # curr = head

        # for _ in range(k):
        #     nextNode = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextNode        
        
        # head.next = self.reverseKGroup(curr, k)

        # return prev
