# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # will generate all possible BSTs with val_list being the unique values of nodes in the BST
    #   requires that val_list is non-decreasing
    def generateTrees_array(self, val_list):
        res = []
        length = len(val_list)
        if length == 0:
            return [None]
        if length == 1:
            return[TreeNode(val_list[0])]
        # for each value in val_list, let it be the root
        for i in range(length):
            root = val_list[i]
            # recursively get the possible left trees
            for left_tree in self.generateTrees_array(val_list[:i]):
                # recursively get the possible right tree
                for right_tree in self.generateTrees_array(val_list[i + 1:]):
                    cur_tree = TreeNode(root, left_tree, right_tree)
                    res.append(cur_tree)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # get all node values we need to cover
        val_list = []
        for val in range(1, n + 1):
            val_list.append(val)
        return self.generateTrees_array(val_list)
