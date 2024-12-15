class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # put freqs of each number in a dict
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        # then look thru this dict and get total max freqs
        ret = 0
        max_freq = 0
        for num in num_dict:
            cur_freq = num_dict[num]
            if cur_freq > max_freq:
                max_freq = cur_freq
                ret = cur_freq
            elif cur_freq == max_freq:
                ret += cur_freq
        return ret
