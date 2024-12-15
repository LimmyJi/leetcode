# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # sums[i] will be the sum of all nodes of lvl i (root has lvl of 0)
        sums = [0]
        bfs = [(root, 0)]
        bfs_pos = 0
        # use bfs to fill out sums
        while bfs_pos < len(bfs):
            cur_node = bfs[bfs_pos][0]
            cur_lvl = bfs[bfs_pos][1]

            if len(sums) == cur_lvl:
                sums.append(0)
            sums[cur_lvl] = sums[cur_lvl] + cur_node.val

            if cur_node.right:
                bfs.append((cur_node.right, cur_lvl + 1))
            if cur_node.left:
                bfs.append((cur_node.left, cur_lvl + 1))
            bfs_pos = bfs_pos + 1
        
        # bfs again, to update node vals
        bfs = [(root, 0)]
        bfs_pos = 0
        while bfs_pos < len(bfs):
            cur_node = bfs[bfs_pos][0]
            cur_lvl = bfs[bfs_pos][1]
            
            # for each inner node, update vals of its children by taking it's childrens
            #   lvl sums and subtracting the childrens vals
            if cur_lvl > 0 and cur_lvl < len(sums) - 1:
                new = sums[cur_lvl + 1]
                if cur_node.right:
                    new = new - cur_node.right.val
                if cur_node.left:
                    new = new - cur_node.left.val
                if cur_node.right:
                    cur_node.right.val = new
                if cur_node.left:
                    cur_node.left.val = new
            # for root node (lvl 0), set its vals and its childrens vals to 0, since no cousisn
            elif cur_lvl == 0:
                cur_node.val = 0
                if cur_node.right:
                    cur_node.right.val = 0
                if cur_node.left:
                    cur_node.left.val = 0

            if cur_node.right:
                bfs.append((cur_node.right, cur_lvl + 1))
            if cur_node.left:
                bfs.append((cur_node.left, cur_lvl + 1))
            bfs_pos = bfs_pos + 1

        return root
