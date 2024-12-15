class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # bs = # of b found
        bs = 0
        # cur is current min # of deletions
        cur = 0
        for char in s:
            # if an a is found, it is either deleted, or all b's before it are
            if char == 'a':
                cur = min(cur + 1, bs)
            else:
                bs += 1
        return cur
