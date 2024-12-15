# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
             return TreeNode(val=val, left=root)
        # bfs
        queue = []
        queue.append((root, 1))
        q_pos = 0
        while q_pos < len(queue):
            cur_depth = queue[q_pos][1]
            cur_node = queue[q_pos][0]
            if cur_depth < depth:
                # if the next depth is the desired depth level, set up the new
                #   nodes with value val, and insert them as children of current node
                if cur_depth == depth - 1:
                    new_left = TreeNode(val=val,left=cur_node.left)
                    new_right = TreeNode(val=val,right=cur_node.right)
                    cur_node.left = new_left
                    cur_node.right = new_right
                else:
                    # else continue the bfs for the desired depth
                    if cur_node.left:
                        queue.append((cur_node.left, cur_depth + 1))
                    if cur_node.right:
                        queue.append((cur_node.right, cur_depth + 1))
            q_pos += 1
        return root
