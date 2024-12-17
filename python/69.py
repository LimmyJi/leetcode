class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lower = 0
        upper = 46340  # since x <= 2^31 - 1
        # binary search within the upper/lower bounds
        while lower != upper - 1 and lower != upper:
            middle = (lower + upper) / 2
            if middle * middle == x:
                return middle
            if middle * middle < x:
                lower = middle
            elif middle * middle > x:
                upper = middle
        # now the sqrt is either upper + 1 or upper, just do casewise check
        if (upper + 1) * (upper + 1) == x:
            return upper + 1
        if upper * upper <= x:
            return upper
        return lower
