class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # answer can only be 1, 2, ..., len(nums) except in special case, mark non-positives
        #   as len(nums) + 1 for ease of use as they can never be the answer
        length = len(nums)
        for i in range(length):
            if nums[i] <= 0:
                nums[i] = length + 1
        # now each num in nums is positive
        # for each num in nums: if it is a suitable answer (less than len(nums)),
        #   then mark it as found in nums, by making the num stored at its index negative
        for i in range(length):
            cur = nums[i]
            if cur < 0:
                cur = -cur
            if cur <= length and nums[cur - 1] >= 0:
                nums[cur - 1] *= -1
        # now at this point, the first positive index we run into can be mapped to the
        #   smallest integer not found in nums
        for i in range(length):
            if nums[i] > 0:
                return i + 1
        # special case, if nums = [1, 2, ..., len(nums)], then return len(nums) + 1
        return length + 1
