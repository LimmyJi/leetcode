class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # easy way
        # return len(s.split()[-1])

        ret = 0
        for i in range(len(s)):
            c = s[i]
            # if we find a space, this might indicate a new word
            if c == ' ':
                # it is a new word if the char after it is not a space
                if i + 1 < len(s) and s[i + 1] != ' ':
                    ret = 0
            else:
                ret += 1
        return ret
        