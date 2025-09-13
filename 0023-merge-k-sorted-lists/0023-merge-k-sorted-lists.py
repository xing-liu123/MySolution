# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from itertools import count

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # # if len(lists) == 0:
        # #     return None
        # # elif len(lists) == 1:
        # #     return lists[0]
        

        # # mid = len(lists) // 2

        # # left = self.mergeKLists(lists[:mid])
        # # right = self.mergeKLists(lists[mid:])

        # # def merge(node1, node2):
        # #     dummy = ListNode()
        # #     curr = dummy

        # #     while node1 or node2:
        # #         if not node1:
        # #             curr.next = node2
        # #             break
        # #         elif not node2:
        # #             curr.next = node1
        # #             break
        # #         else:
        # #             if node1.val <= node2.val:
        # #                 curr.next = node1
        # #                 curr = curr.next
        # #                 node1 = node1.next
        # #             else:
        # #                 curr.next = node2
        # #                 curr = curr.next
        # #                 node2 = node2.next

        # #     return dummy.next

        # # return merge(left, right)
        # counter = count()
        # heap = [(node.val, next(counter), node) for node in lists if node]
        # heapq.heapify(heap)
        # dummy = ListNode()
        # curr = dummy

        # while heap:
        #     _, _, node = heapq.heappop(heap)
        #     curr.next = node
        #     curr = curr.next

        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, next(counter), node.next))

        # return dummy.next

        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        leftCurr = left
        rightCurr = right
        dummy = ListNode(-1)
        curr = dummy

        while leftCurr and rightCurr:
            if leftCurr.val < rightCurr.val:
                curr.next = leftCurr
                leftCurr = leftCurr.next
            else:
                curr.next = rightCurr
                rightCurr = rightCurr.next
            
            curr = curr.next
        
        if leftCurr:
            curr.next = leftCurr
        
        if rightCurr:
            curr.next = rightCurr

        return dummy.next
            






