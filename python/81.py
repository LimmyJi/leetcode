class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return True
            if nums[left] <= nums[pivot]:
                if nums[left] == nums[pivot]:
                    if self.search(nums[left:pivot], target):
                        return True
                if nums[pivot] >= target and nums[left] <= target:
                    right = pivot
                else:
                    left = pivot + 1
            elif nums[right] >= nums[pivot]:
                if nums[pivot] <= target and nums[right] >= target:
                    left = pivot
                else:
                    right = pivot - 1
        return False
