#include <stddef.h>

// Definition for a Node.
struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* postorder(struct Node* root, int* returnSize) {
    int* ret = malloc(sizeof(int) * 1);
    int max_ret_size = 1;
    *returnSize = 0;
    if (!root){
        return ret;
    }
    // dfs with stack
    // visted[i] will keep track of how many children of stack[i] that
    //   we have visted
    struct Node* stack[10000] = {NULL};
    int visited[10000] = {0};
    stack[0] = root;
    visited[0] = 0;
    int stack_size = 1;
    int stack_pos = 0;
    while (stack_pos < stack_size){
        struct Node* cur = stack[stack_pos];
        struct Node** children = cur -> children;
        int num_children = cur -> numChildren;
        if (num_children > visited[stack_pos]){
            stack[stack_size] = children[visited[stack_pos]];
            visited[stack_pos]++;
            visited[stack_size] = 0;
            stack_size ++;
            stack_pos++;
        }
        // add the node to ret if we have visted all its children
        else {
            ret[*returnSize] = stack[stack_pos] -> val;
            *returnSize = *returnSize + 1;
            if (*returnSize == max_ret_size){
                ret = realloc(ret, sizeof(int) * max_ret_size * 2);
                max_ret_size = max_ret_size * 2;
            }
            if (stack_pos > 0){
                stack_pos--;
            }
            if (stack_size > 0){
                stack_size--;
            }
        }
    }
    return ret;
}
