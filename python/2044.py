from itertools import combinations

class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the max bitwise or would be the bitwise or of the whole array
        maximum = nums[0]
        for num in nums[1:]:
            maximum = maximum | num
        
        ret = 0
        # get all possible subsets, and see if their bitwise or is same as maximum
        for r in range(1, len(nums)):
            subsets = combinations(nums, r)
            for s in subsets:
                cur = s[0]
                for num in s[1:]:
                    cur = cur | num
                if cur == maximum:
                    ret = ret + 1
        return ret + 1
