class Solution(object):
    def abs_val(self, n):
        if n < 0:
            return -n
        return n

    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # use dicts to keep track of present letters
        s_dict = {}
        t_dict = {}
        res = 0
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else:
                t_dict[letter] += 1
        # then go through the dicts and find missing letters
        for letter in s_dict:
            if letter in t_dict:
                res += self.abs_val(s_dict[letter] - t_dict[letter])
            else:
                res += s_dict[letter]
        for letter in t_dict:
            if letter not in s_dict:
                res += t_dict[letter]

        return res
