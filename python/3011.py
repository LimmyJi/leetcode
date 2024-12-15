class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # make a copy of nums, and an array of indexs
        nums_og = []
        indexs = []
        for i in range(len(nums)):
            nums_og.append(nums[i])
            indexs.append(i)
        # for each index i, find the i-th smallest element and its OG index
        for i in range(len(nums)):
            minimum = nums[i]
            min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    minimum = nums[j]
                    min_index = j
            nums[min_index] = nums[i]
            nums[i] = minimum
            minimum = indexs[min_index]
            indexs[min_index] = indexs[i]
            indexs[i] = minimum
        # use the recorded indexes to see if all nums in between have same set bits
        for i in range(len(indexs)):
            if bin(nums_og[i]).count("1") != bin(nums_og[indexs[i]]).count("1"):
                return False
            for n in nums_og[min(i, indexs[i]) + 1: max(i, indexs[i])]:
                if bin(nums_og[i]).count("1") != bin(n).count("1"):
                    return False
        return True
