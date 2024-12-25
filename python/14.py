class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        while (1):
            # always try to add the next letter of the first str in strs to
            #   our ans
            if len(strs[0]) != 0:
                ans += (strs[0][0])
            else:
                return ans
            # now make sure that adding this letter to ans is a valid addition
            for i in range (len(strs)):
                # if we find an empty string, new letter doesnt belong
                if len(strs[i]) == 0:
                    ans = ans[:-1]
                    return ans
                # if new letter doesnt match, it doesnt beling
                if strs[i][0] != ans[-1]:
                    ans = ans[:-1]
                    return ans
                # else shorten the string by its first letter
                strs[i] = strs[i][1:]
