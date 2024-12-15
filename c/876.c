// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

// get how many nodes in the ll recursively
int how_many(const struct ListNode* head, int counter){
    if (!(head->next)){
        return counter;
    }
    else{
        return how_many(head->next, counter + 1);
    } 
}

struct ListNode* middleNode(const struct ListNode* head){
    // get pos of middle based on how many nodes in the ll
    int count = how_many(head, 1);
    int middle = count / 2 + 1;
    struct ListNode* ans = head;
    // traverrse ll till middle is reached
    for (int i = 1; i < middle; i++){
        ans = ans->next;
    }
    return ans;
}
