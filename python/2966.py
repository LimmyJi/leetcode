class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        nums.sort()
        cur_array = []
        # within the sorted array, create triplets
        #   since its sorted, we have the lowest possible differences
        for num in nums:
            for cur_num in cur_array:
                if abs(cur_num - num) > k:
                    return []
            cur_array.append(num)
            if len(cur_array) == 3:
                ret.append(cur_array)
                cur_array = []
        return ret
