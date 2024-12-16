class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        # modified binary search, note that after every step we will still have a mini rotated sorted array
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return True
            if nums[left] <= nums[pivot]:
                # if nums[left] == nums[pivot], we have found a smaller rotated sorted array
                #   search this one instead
                if nums[left] == nums[pivot]:
                    if self.search(nums[left:pivot], target):
                        return True
                # this is the normal binary search case where we can set right to the pivot
                if nums[pivot] >= target and nums[left] <= target:
                    right = pivot
                else:
                    # else, if target < nums[left] or nums[pivot] < target, make left smaller so that
                    #   we get closer to base case
                    left = pivot + 1
            # if nums[left] > nums[pivot] and nums[right] >= nums[pivot]
            elif nums[right] >= nums[pivot]:
                # if nums[pivot] <= target <= nums[right] and nums[pivot] < nums[left]
                #   make left = pivot, so that we have nums[left] <= target <= nums[right] (normal binary search case)
                if nums[pivot] <= target and nums[right] >= target:
                    left = pivot
                else:
                    right = pivot - 1
        return False
