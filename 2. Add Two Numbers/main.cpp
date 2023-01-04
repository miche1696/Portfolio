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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        bool l1f = true , l2f = true;   // Two flags that will be used to understand if the number l1 or l2 currently pointing to the last node. 
        int sum = 0;
        ListNode* retVal = new ListNode();
        ListNode* head = retVal;


        while(l1f || l2f){    // The logic is to continue cycling until both flags are false. Flags will became false once the l1 or l2 pointers reach to the end of the list
            if(l1f){
                sum += l1->val;
                l1=l1->next;
                if (l1==nullptr){
                    l1f = false;
                }
            }
            if(l2f){
                sum += l2->val;
                l2=l2->next;
                if (l2==nullptr){
                    l2f = false;
                }
            }
            ListNode* newnode = new ListNode(sum%10);
            retVal->next=newnode;
            retVal=retVal->next;
            if (sum>9) sum=1;
            else sum=0;
        }
        if(sum) 
        {
            ListNode* newnode = new ListNode(sum%10);
            retVal->next=newnode;
            retVal=retVal->next;
        }
        return head->next;

    }
};