class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 1
        while ret <= n:
            # 1 + 2 + ... + x-1 = (x-1)(x)/2, and x+1 + ... + n = (n-x)(n-x+1)/2 + (n-x)*x
            if (ret - 1) * ret / 2 == (n - ret) * (n - ret + 1) / 2 + (n - ret) * ret:
                return ret
            ret += 1
        return -1
