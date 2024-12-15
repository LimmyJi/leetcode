class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dict that keeps track of chars in s, and their freqs
        count_dict = {}
        for c in s:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1
        ans = ""

        # constantly find char with highest freq in count_dict, and
        #   append it to ans # of times according to its freq
        while len(count_dict) >= 1:
            cur_count = 0
            cur_c = ''
            for c in count_dict:
                if count_dict[c] > cur_count:
                    cur_count = count_dict[c]
                    cur_c = c
            count_dict.pop(cur_c)
            ans += cur_c * cur_count
        return ans
