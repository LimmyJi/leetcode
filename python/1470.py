class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ret = []
        # will keep track of position of y_n's in the array
        half = len(nums)/2
        for i in range(half):
            ret.append(nums[i])
            ret.append(nums[i + half])
        return ret
