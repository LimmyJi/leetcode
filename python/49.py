class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret_dict = {}
        # hashmap, where the hash function is sorting each string
        #  alphabetically
        for s in strs:
            ss = str(sorted(s))
            if ss in ret_dict:
                ret_dict[ss].append(s)
            else:
                ret_dict[ss] = [s]
        ret = []
        for ss in ret_dict:
            ret.append(ret_dict[ss])
        return ret
