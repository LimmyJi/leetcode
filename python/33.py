class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # similar input and question to 81, but we are not allowed duplicate values
        #   since the logic in 81 can handle duplicate values aswell as non-duplicates,
        #   can use the same logic as 81, except we need to return indexs instead
        #   of True/False
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if nums[left] <= nums[pivot]:
                if nums[pivot] >= target and nums[left] <= target:
                    right = pivot
                else:
                    left = pivot + 1
            elif nums[right] >= nums[pivot]:
                if nums[pivot] <= target and nums[right] >= target:
                    left = pivot
                else:
                    right = pivot - 1
        return -1
