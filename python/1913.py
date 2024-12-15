class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = 0
        max_2 = 0
        min_1 = 10001
        min_2 = 10001
        # max will be (largest * 2nd largest) - (smallest * 2nd smallest)
        for num in nums:
            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_2 = num
            if num < min_1:
                min_2 = min_1
                min_1 = num
            elif num < min_2:
                min_2 = num
        return max_1 * max_2 - min_1 * min_2
