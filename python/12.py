class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        # how many 1000's fit
        thousands = num // 1000
        for i in range(0, thousands):
            ans = ans + "M"
        # for the rest of the powers of 10 (1, 10, 100), get their counts
        #   if the count is 4 or 9, there are special cases (subtractive forms)
        #   if the count is greater than 5, then we can use the 5X numerals
        #   then, after these 2 rules we can use the normal symbols
        # 100s
        hundreds = (num - thousands * 1000) // 100
        if hundreds == 4:
            ans = ans + "CD"
        elif hundreds == 9:
            ans = ans + "CM"
        else:
            if hundreds >= 5:
                ans = ans + "D"
            for i in range(0, hundreds % 5):
                ans = ans + "C"
        # 10s
        tens = (num - thousands * 1000 - hundreds * 100) // 10
        if tens == 4:
            ans = ans + "XL"
        elif tens == 9:
            ans = ans + "XC"
        else:
            if tens >= 5:
                ans = ans + "L"
            for i in range(0, tens % 5):
                ans = ans + "X"
        # 1s
        ones = num % 10
        if ones == 4:
            ans = ans + "IV"
        elif ones == 9:
            ans = ans + "IX"
        else:
            if ones >= 5:
                ans = ans + "V"
            for i in range(0, ones % 5):
                ans = ans + "I"
            
        return ans
