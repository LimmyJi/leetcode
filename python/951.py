# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        if (root1 and root2) or (not root1 and not root2):
            if root1:
                if root1.val == root2.val:
                    # either the left/right subtrees have been flipped, or not
                    # one of these cases must be true if root1 and root2 are flip equiv
                    case1 = (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
                    case2 = (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
                    return case1 or case2
                # if root1 and root2 dont have same values in root, return False
                return False
            # if both root1 and root2 are empty trees, return True
            return True
        # if root1 is nonempty and root2 is empty, or vice versa, return False
        return False
