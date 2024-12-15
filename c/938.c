
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int rangeSumBST(struct TreeNode* root, int low, int high){
    if (!(root)){
        return 0;
    }
    else{
        // recurse on children, adding the value of the root if it falls in the range
        if (low <= root->val && root->val <= high){
            return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
        }
        else{
            return rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
        }
    }
}
