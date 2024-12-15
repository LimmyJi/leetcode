// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

void deleteNode(struct ListNode* node) {
    struct ListNode* prev = NULL;
    struct ListNode* cur = node;
    struct ListNode* next_node = node->next;
    while (next_node){
        // shift values of nodes that come after node
        cur->val = next_node->val;
        prev = cur;
        cur = next_node;
        next_node = next_node->next;
    }
    // delete last node as now it is dupe
    prev->next = NULL;
}
