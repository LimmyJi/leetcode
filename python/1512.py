class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # keep track of number counts in a dict
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
        
        # if there are n instances of a number, there are exactly
        #   1 + 2 + ... + n-1 = n * (n-1) / 2 good pairs of the number
        ret = 0
        for num in lookup:
            if lookup[num] > 1:
                ret += lookup[num] * (lookup[num] - 1) / 2
        return ret
        