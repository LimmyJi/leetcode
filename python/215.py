class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # can also use priotiy queue
        nums.sort()
        return nums[len(nums) - k]
