/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;


        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode head2 = reverse(slow);

        int max = 0;
        while (head != null && head2 != null) {
            max = Math.max(head.val + head2.val, max);
            head = head.next;
            head2 = head2.next;
        }

        return max;
            

    }

    private ListNode reverse(ListNode head) {
        ListNode temp = null;
        ListNode prev = null;

        while (head != null) {
            temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }
}