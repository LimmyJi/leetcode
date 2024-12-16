// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    // count the nodes in A, and in B
    struct ListNode *currentA = headA;
    int countA = 0;
    while (currentA){
        countA++;
        currentA = currentA->next;
    }
    struct ListNode *currentB = headB;
    int countB = 0;
    while (currentB){
        countB++;
        currentB = currentB->next;
    }
    // traverse nodes in A/B (whichever has more nodes)
    //   until the # of nodes left to traverse in each ll is the same
    struct ListNode *currentA2 = headA;
    while (countA > countB){
        countA--;
        currentA2 = currentA2->next;
    }

    struct ListNode *currentB2 = headB;
    while (countB > countA){
        countB--;
        currentB2 = currentB2->next;
    }
    // traverse the lls together until we find an intersection
    struct ListNode* ans = NULL;
    while (countA){
        if (currentB2 == currentA2){
            ans = currentA2;
            break;
        }
        currentA2 = currentA2->next;
        currentB2 = currentB2->next;
        countA--;
        countB--;
    }
    return ans;
}
