class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length_nums = len(nums)
        if length_nums == 1:
            return[nums]
        res = []
        # for each num, get all the permutations where num is the
        #   last element
        for i in range(length_nums):
            # do this recursively, get all permutations without num,
            #   then add num to the end
            perm_no_i = self.permute(nums[:i] + nums[i + 1:])
            for perm in perm_no_i:
                res.append(perm + [nums[i]])
        return res
