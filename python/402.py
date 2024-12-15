class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return num
        elif k == len(num):
            return '0'

        # digits not deleted will be added to stack
        stack = []
        for digit in num:
            # if we can delete a digit, and the prev digit is greater than
            #   the current digit, delete it
            #   keep doing run out of deletes, or we cant delete anymore
            while k > 0 and stack and digit < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(digit)

        # if we have leftover deletes, this means that the digits are in non-decreasing
        #   order, so just delete from top of stack
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        # convert from list to string
        temp = ''
        for i in stack:
            temp += i

        # to remove leading 0s
        temp = int(temp)
        return str(temp)
