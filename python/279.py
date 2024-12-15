from math import sqrt

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        INFINITY = 10001
        # stepwise[i] represents min # of PS in i+1's sum
        stepwise = [0 for _ in range(n)]
        stepwise[0] = 1
        for i in range(1, n):
            # if i+1 is a PS, it is the sum of 1 PS
            if int(sqrt(i + 1)) * int(sqrt(i + 1)) == i + 1:
                stepwise[i] = 1
            else:
                # if i+1 is not a PS, try out possible sums of 1+1, 2+i-1, ...
                #   and use dp to find lowest number of PS that add up to i
                cur_ans = INFINITY
                left = 0
                right = i - 1
                to_add = 3
                while left <= right:
                    if stepwise[left] + stepwise[right] < cur_ans:
                        cur_ans = stepwise[left] + stepwise[right]
                    left += to_add
                    right -= to_add
                    to_add += 2
                stepwise[i] = cur_ans
        return stepwise[n-1]
