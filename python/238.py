class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        current_product = 1
        # ret[n] = nums[0] * nums[1] * ... * nums[n-1]
        ret = [1 for _ in nums]
        for i in range(length):
            ret[i] *= current_product
            current_product *= nums[i]

        # now multiply ret[n] by nums[len(nums) - 1] * ... * nums[n + 1]
        # now ret is exactly what we need to return
        current_product = 1
        for i in range(length):
            ret[length - 1 - i] *= current_product
            current_product *= nums[length - 1 - i]
        return ret
