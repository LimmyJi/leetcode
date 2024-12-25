class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # now assume x is positive
        # power_of_10 will be the largest power of 10 that is smaller than x
        power_of_10 = 1
        while x // power_of_10 > 9:
            power_of_10 *= 10
        x1 = x
        x2 = 0
        # extract least significant digits from x using modulo 10, then
        #   construct x2 by making these digits the most significant in x2
        while x1 != 0:
            digit = x1 % 10
            x2 += digit * power_of_10
            power_of_10 /= 10
            x1 -= digit
            x1 /= 10
        # palindrome number iff the i-th most significant digit is equal to the
        #   i-th least significant digit, which is what we have constructed in x2
        if x2 == x:
            return True
        return False
