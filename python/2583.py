# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # sums[i] will represent sum of i-th lvl
        sums = [0]
        max_level = 0
        bfs = [(root, 0)]
        bfs_pos = 0
        # use bfs to fill out sums
        while bfs_pos < len(bfs):
            cur_node = bfs[bfs_pos][0]
            cur_level = bfs[bfs_pos][1]
            sums[cur_level] = sums[cur_level] + cur_node.val

            if cur_node.right:
                bfs.append((cur_node.right, cur_level + 1))
            if cur_node.left:
                bfs.append((cur_node.left, cur_level + 1))
            if cur_level + 1 > max_level:
                sums.append(0)
                max_level = max_level + 1

            bfs_pos = bfs_pos + 1

        # extract k-th largest lvl sum
        sums.sort()

        if k > len(sums) or sums[-k] == 0:
            return -1
        return sums[-k]
        