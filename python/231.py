class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # cant be negative
        if n < 1:
            return False
        # divide by 2 until we get odd number, or we reach 1
        while n != 1:
            if n % 2:
                return False
            n = n / 2
        return True
