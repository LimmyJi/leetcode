class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        res = []
        pos_in_nums2 = 0
        # for each num in nums1
        for i in range(m):
            # append the nums in nums2 that are leq to it, before adding it
            while pos_in_nums2 < n and nums1[i] > nums2[pos_in_nums2]:
                res.append(nums2[pos_in_nums2])
                pos_in_nums2 += 1
            res.append(nums1[i])
        # if there are still nums in nums2, add them to the end of ret
        if pos_in_nums2 < n:
            res += nums2[pos_in_nums2:]
        # update nums1, because of how we are returning the results
        for i in range(m + n):
            nums1[i] = res[i]
