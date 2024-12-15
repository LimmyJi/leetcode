class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        # 1s to front, 0s to back
        for c in s:
            if c == '1':
                ret = c + ret
            else:
                ret = ret + c
        # remove a 1 from front and append to back
        #   since has to be odd
        ret += ret[0]
        ret = ret[1:]
        return ret
