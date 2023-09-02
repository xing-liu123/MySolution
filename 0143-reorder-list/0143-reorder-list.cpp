/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = NULL;
        ListNode* temp = NULL;

        while (head != NULL) {
            temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }

        return prev;
    }
    void reorderList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return;
        }

        ListNode* prev = head;
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast != NULL && fast->next != NULL) {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }

        prev->next = NULL;
        ListNode* right = reverse(slow);
        ListNode* left = head;

        ListNode* dummy = new ListNode();
        ListNode* curr = dummy;

        while(left != NULL || right != NULL) {
            if(left != NULL) {
                curr->next = left;
                left = left->next;
                curr = curr->next;
            }

            if (right != NULL) {
                curr->next = right;
                right = right->next;
                curr = curr->next;
            }
        }

        head = dummy->next;
    }
};