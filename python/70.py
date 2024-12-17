class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [0] * n
        # base case step 1
        table[0] = 1
        for i in range (1, n):
            # base case step 2
            if i == 1:
                table[1] = 2
            else:
                # for the i-th step, we either take 1 step from step i - 1
                #   or 2 steps from step i - 2
                table[i] = table[i - 2] + table[i - 1]
        return table[-1]
