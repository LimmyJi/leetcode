# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # bfs
        ret = 0
        queue = []
        queue.append(root)
        q_pos = 0
        while q_pos < len(queue):
            cur = queue[q_pos]
            # add right child to queue if it exists
            if cur.right is not None:
                queue.append(cur.right)
            # check if left child is leaf, if not add to queue
            if cur.left is not None:
                if cur.left.left is None and cur.left.right is None:
                    ret += cur.left.val
                else:
                    queue.append(cur.left)
            q_pos += 1
        return ret
