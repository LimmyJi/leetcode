# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# can speed up with dp
class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ans = []
        # no such thing as a FBT with even node count
        if n % 2 == 0 or n < 1:
            return ans
        if n == 1:
            return [TreeNode()]
        # a FBT with n nodes will consist of a root node, with its left child being a FBT with i nodes,
        #   and its right child being an FBT with n - i - 1 nodes, where n is odd and i is odd, i < n
        for i in range(1, n, 2):
            for leftTree in self.allPossibleFBT(i):
                for rightTree in self.allPossibleFBT(n - i - 1):
                    newTree = TreeNode()
                    newTree.left = leftTree
                    newTree.right = rightTree
                    ans.append(newTree)

        return ans
