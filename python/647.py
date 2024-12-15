class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        size = 1
        # brute force approach, could be better with dp
        while size <= len(s):
            for start in range(len(s) - size + 1):
                if s[start:start+size] == s[start:start+size][::-1]:
                    ans += 1
            size += 1
        return ans
        