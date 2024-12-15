class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        ret = 0
        while i + 1 < len(s):
            # add the score of these adjacent characters
            ret += abs(ord(s[i]) - ord(s[i+1]))
            i += 1
        return ret
