# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        stack = []
        ret = ""
        stack.append([root, 0])
        # use dfs, note that in the stack, a node can only go ontop of its parent unless root
        while len(stack):
            cur = stack[-1]
            # if we reach a leaf, determine if the string starting from this leaf
            #   going back to the root is lexicographically smaller than current string
            if cur[0].left is None and cur[0].right is None:
                cur_str = ""
                for c in stack[::-1]:
                    cur_str += chr(c[0].val + 97)
                if ret == "" or cur_str < ret:
                    ret = cur_str
                stack.pop(-1)
            else:
                # cur[1] = 0 if cur[0] hasnt had its children visited
                # = 1 if cur[0].left has been visited
                # = 2 if cur[0].left and .right have been visited 
                #   OR if .left is None and .right has been visited
                if cur[1] == 0:
                    if cur[0].left is not None:
                        cur[1] = 1
                        stack.append([cur[0].left,0])
                    else:
                        cur[1] = 2
                        stack.append([cur[0].right,0])
                elif cur[1] == 1:
                    if cur[0].right is not None:
                        stack.append([cur[0].right,0])
                    cur[1] = 2
                elif cur[1] == 2:
                    stack.pop(-1)
        return ret
