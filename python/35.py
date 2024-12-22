class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        left = 0
        right = len_nums
        # binary search to try and find target
        while left != right:
            middle = (left + right) / 2
            if nums[middle] == target:
                return middle
            if middle > 0 and middle < len_nums:
                if nums[middle - 1] < target and nums[middle] > target:
                    return middle
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = max(0, middle - 1)
        # if target is not found, the final position of left == right should
        #   be where we find target
        return left
