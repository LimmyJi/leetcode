class Solution(object):
    # scuffed version of mergesort (i dont count len as built in func)
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # base case
        n = len(nums)
        if n <= 1:
            return nums

        # split nums in half
        left = nums[:n // 2]
        right = nums[n // 2:]
        # sort each half recursively
        left = self.sortArray(left)
        right = self.sortArray(right)
        # merge the 2 halves using the fact that they are sorted
        ret = []
        left_pos = 0
        right_pos = 0
        while left_pos < len(left) or right_pos < len(right):
            if right_pos >= len(right):
                ret = ret + left[left_pos:]
                break
            elif left_pos >= len(left):
                ret = ret + right[right_pos:]
                break

            elif left[left_pos] < right[right_pos]:
                ret.append(left[left_pos])
                left_pos = left_pos + 1

            elif right[right_pos] <= left[left_pos]:
                ret.append(right[right_pos])
                right_pos = right_pos + 1

        return ret
