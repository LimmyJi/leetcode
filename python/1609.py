# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # use bfs starting from root, keeping track of level
        queue = [(root, 0)]
        q_pos = 0
        while len(queue) > q_pos:
            cur = queue[q_pos]
            # see if parity of level is opposite of parity of node value
            if cur[0].val % 2 == cur[1] % 2:
                return False
            if cur[0].left is not None:
                queue.append((cur[0].left, cur[1] + 1))
            if cur[0].right is not None:
                queue.append((cur[0].right, cur[1] + 1))
            q_pos += 1
            # check the next node in the queue, and see if the parity rules of the level line up
            if len(queue) > q_pos:
                new = queue[q_pos]
                if new[1] == cur[1]:
                    level = cur[1]
                    if level % 2 == 1 and cur[0].val <= new[0].val:
                        return False
                    elif level % 2 == 0 and cur[0].val >= new[0].val:
                        return False
        return True
            