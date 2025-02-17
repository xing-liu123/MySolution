# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(len(lists))
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        

        mid = len(lists) // 2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        def merge(node1, node2):
            dummy = ListNode()
            curr = dummy

            while node1 or node2:
                if not node1:
                    curr.next = node2
                    break
                elif not node2:
                    curr.next = node1
                    break
                else:
                    if node1.val <= node2.val:
                        curr.next = node1
                        curr = curr.next
                        node1 = node1.next
                    else:
                        curr.next = node2
                        curr = curr.next
                        node2 = node2.next

            return dummy.next

        return merge(left, right)
                





