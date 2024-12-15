class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        index = []  # keep track of currently found '('s
        to_remove = []  # keep track of indexes to be removed
        for i in range(len(s)):
            if s[i] == '(':
                index.append(i)
            elif s[i] == ')':
                # if we find a ')', attempt to match it up with a '('
                #   if we cant, then remove it
                if len(index) == 0:
                    to_remove.append(i)
                else:
                    index = index[1:]
        # remove the remaining unmatched '('s
        to_remove += index
        # return s, but without any indexes in to_remove
        ret = ""
        for i in range(len(s)):
            if len(to_remove) == 0 or i != to_remove[0]:
                ret += s[i]
            else:
                to_remove = to_remove[1:]
        return ret
