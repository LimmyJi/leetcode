class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        # base cases
        if n < k:
            return res
        if k == 1:
            for i in range (n):
                res.append([i + 1])
            return res
        else:
            # recursion, each combo either has n as an element, or not
            #   since params keep decreasing, we will eventually get to base cases
            for combo in self.combine(n - 1, k - 1):
                combo.append(n)
                res.append(combo)
            res += self.combine(n - 1, k)
            return res
