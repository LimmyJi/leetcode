class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        # x[i] will represent the polarity (even or odd) of
        #   the i-th segment of s
        x = []
        cur_count = 1
        cur_c = s[0]
        for c in s[1:]:
            if c == cur_c:
                cur_count += 1
            else:
                x.append(cur_count % 2)
                cur_count = 1
                cur_c = c
        x.append(cur_count % 2)

        ret = 0
        if len(x) == 1:
            return ret
        # in 1 change, we will switch polarity of both segment i and i + 1
        #   keep doing this, to see if we can get polarity of all to be 0
        for i in range(len(x)):
            if x[i]:
                ret += 1
                if x[i + 1] == 0:
                    x[i + 1] = 1
                else:
                    x[i + 1] = 0
        return ret
