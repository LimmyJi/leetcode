# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0
        queue = []
        pos = 0
        queue.append((root, root.val))
        # bfs, which also keeps track of root-to-leaf path
        while pos < len(queue):
            cur = queue[pos][0]
            # if we found a root, add its root-to-leaf path to ret
            if cur.left is None and cur.right is None:
                ret += queue[pos][1]
            
            if cur.left is not None:
                queue.append((cur.left, queue[pos][1] * 10 + cur.left.val))

            if cur.right is not None:
                queue.append((cur.right, queue[pos][1] * 10 + cur.right.val))

            pos += 1
        return ret
