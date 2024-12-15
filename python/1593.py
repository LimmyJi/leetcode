import itertools

class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexs = range(1, len(s))  # 1, 2, ..., len(s) - 1
        for i in range(1, len(s)):
            added = 0
            # divisors will consist of all possible ways to divide s into substrings,
            #   each way is represented as an array, with each array element indicating there
            #   is a divisor before the given position
            divisors = itertools.combinations(indexs, i)
            for div in divisors:
                # go through each divisor, see if each substring is unique
                x = {}
                x[s[0:div[0]]] = 1

                for j in range(1, len(div)):
                    if s[div[j - 1]:div[j]] in x:
                        break
                    else:
                       x[s[div[j - 1]:div[j]]] = 1
                
                if s[div[-1]:] not in x:
                    x[s[div[-1]:]] = 1

            # we check divisors from largest to smallest, so break as soon as a valid partition is found
                if len(x.keys()) == i + 1:
                    added = 1
                    break
            if added == 0:
                return i
        return len(s)
