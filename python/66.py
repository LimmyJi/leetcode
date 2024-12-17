class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # add 1 and perform carry-over
        #   if we added 1 somewhere here, done
        for i in range(1, len(digits)):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                return digits
        # else if we havent added 1 anywhere, and the leading digit
        #   is a 9, carry over to an extra 1 in front
        if digits[0] == 9:
            digits[0] = 0
            digits = [1] + digits
        else:
            digits[0] += 1
        
        return digits
