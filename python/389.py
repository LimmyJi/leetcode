class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # lookup of all char in s and their counts
        lookup = {}
        for c in s:
            if c not in lookup:
                lookup[c] = 1
            else:
                lookup[c] = lookup[c] + 1
        
        # go thru t, decrementing lookup[c], if we find a c that
        #   DNE in lookup, or if lookup[c] < 0, then we found odd one out
        for c in t:
            if c not in lookup:
                return c

            lookup[c] = lookup[c] - 1
            if lookup[c] < 0:
                return c
        