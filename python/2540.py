class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0
        # linear search using the fact nums1 and nums2 are sorted
        while i < len1 and j < len2:
            cur1 = nums1[i]
            cur2 = nums2[j]
            if cur1 == cur2:
                return cur1
            elif cur1 < cur2:
                i += 1
            else:
                j += 1
        return -1
