class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        left = 0
        cur = 1
        # assume nums[right] always gets added to current subarray
        for right in range(len(nums)):
            cur *= nums[right]
            # if adding right to subarray results in product >= k,
            #   find new inner subarray such that product >= k
            while left < right and cur >= k:
                cur /= nums[left]
                left += 1
            if cur < k:
                # the only new subarrays we will get are the ones that contain nums[right]
                ret += right - left + 1
        return ret
