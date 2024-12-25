class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        length = len(s)
        for i in range(0 , length):
            # no special cases for adding 1000
            if s[i] == "M":
                ans = ans + 1000
            # or 500
            elif s[i] == "D":
                ans = ans + 500
            # subtract 100 if C comes right before D or M, else add 100
            elif s[i] == "C":
                if i + 1 < length:
                    if s[i + 1] == "M" or s[i + 1] == "D":
                        ans = ans - 100
                    else:
                        ans = ans + 100
                else:
                    ans = ans + 100
            # no special case for L
            elif s[i] == "L":
                ans = ans + 50
            # subtract 10 if X comes right before L or C, else add 10
            elif s[i] == "X":
                if i + 1 < length:
                    if s[i + 1] == "C" or s[i + 1] == "L":
                        ans = ans - 10
                    else:
                        ans = ans + 10
                else:
                    ans = ans + 10
            # no special case for V
            elif s[i] == "V":
                ans = ans + 5
            else:
                # else we have I, subtract 1 if it comes right before V or X, else add 1
                if i + 1 < length:
                    if s[i + 1] == "X" or s[i + 1] == "V":
                        ans = ans - 1
                    else:
                        ans = ans + 1
                else:
                    ans = ans + 1

        return ans
