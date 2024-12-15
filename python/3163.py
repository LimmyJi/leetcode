class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        # go thru word, counting consecutive characters
        ret = []
        cur_count = 1
        cur_c = word[0]
        for c in word[1:]:
            if c == cur_c:
                if cur_count == 9:
                    ret.append(str(cur_count))
                    ret.append(cur_c)
                    cur_count = 1
                else:
                    cur_count += 1
            else:
                ret.append(str(cur_count))
                ret.append(cur_c)
                cur_count = 1
                cur_c = c
        
        # last compression
        ret.append(str(cur_count))
        ret.append(cur_c)
        return "".join(ret)
