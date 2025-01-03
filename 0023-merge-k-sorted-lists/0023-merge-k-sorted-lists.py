# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = ListNode()

        def merge(curr):
            min_node_idx = -1
            for idx, next_node in enumerate(lists):
                if next_node and (min_node_idx == -1 or next_node.val <= lists[min_node_idx].val):
                    min_node_idx = idx

            if min_node_idx == -1:
                return
            
            curr.next = lists[min_node_idx]
            lists[min_node_idx] = lists[min_node_idx].next
            curr = curr.next
            merge(curr)

        merge(node)

        return node.next