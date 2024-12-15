class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # set of nums found in nums1
        set = {}
        for num in nums1:
            if num not in set:
                set[num] = 1
        
        # go thru nums2, see if num is in the set
        #   add to ret and remove from set if so
        ret = []
        for num in nums2:
            if num in set:
                ret.append(num)
                set.pop(num)

        return ret
