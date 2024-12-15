class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1 = version1.split('.')
        list2 = version2.split('.')
        pos1 = 0
        pos2 = 0
        # split list1 and list2 into segments, compare each segments for
        #   inequalities, until we go thru all the segments of one of the lists
        while pos1 < len(list1) and pos2 < len(list2):
            if int(list1[pos1]) < int(list2[pos2]):
                return -1
            if int(list1[pos1]) > int(list2[pos2]):
                return 1
            pos1 += 1
            pos2 += 1
        # if 1 list has remaining non-zero segments, that means it is larger
        if pos1 < len(list1):
            for i in range(pos1, len(list1)):
                if int(list1[i]):
                    return 1
        if pos2 < len(list2):
            for i in range(pos2, len(list2)):
                if int(list2[i]):
                    return -1
        return 0
