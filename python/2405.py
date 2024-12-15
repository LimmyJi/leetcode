class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = ""
        res = 0
        # since we want min # of substrings, if a repeat is found,
        #   start from scratch where it is found
        for letter in s:
            if letter in seen:
                res += 1
                seen = letter
            else:
                seen += letter
        if seen != "":
            res += 1
        return res
