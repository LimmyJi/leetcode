class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # easy way:
        # return 2 * nums
        n = len(nums)
        ret = [0 for _ in range(2 * n)]
        pos1 = 0
        pos2 = n
        # go thru nums, copying to pos1 and pos2 in ret
        while pos1 < n:
            ret[pos1] = nums[pos1]
            ret[pos2] = nums[pos1]
            pos1 += 1
            pos2 += 1
        return ret
