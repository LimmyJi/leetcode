class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n:
            if n < 3:
                return 1
            trib = [0 for _ in range(n + 1)]
            trib[1] = 1
            trib[2] = 1
            # dp, used prev 3 to get current
            for i in range(3, n + 1):
                trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]
            return trib[-1]
        else:
            return 0
