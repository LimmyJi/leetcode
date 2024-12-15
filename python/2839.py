class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # possible swaps: 0 and 2, 1 and 3, can brute force
        if s1 == s2:
            return True
        if s1[2] + s1[1] + s1[0] + s1[3] == s2:
            return True
        if s1[0] + s1[3] + s1[2] + s1[1] == s2:
            return True
        if s1[2] + s1[3] + s1[0] + s1[1] == s2:
            return True
        return False
