class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = 0
        # cur will start off as the score of splitting via:
        #   left = s[0], right = s[1] + ... + s[-1]
        for c in s[1:]:
            if c == '1':
                cur += 1
        if s[0] == '0':
            cur += 1
        ret = cur
        # change the value of the cur score based on position of split
        for c in s[1:-1]:
            if c == '1':
                cur -= 1
            else:
                cur += 1
            if cur > ret:
                ret = cur
        
        return ret
        