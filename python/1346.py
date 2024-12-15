class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # x[n][0] indicates if n has been found
        # x[n][1] indicates if m has been found, where m * 2 = n
        x = {}
        for n in arr:
            if n:
                if n not in x:
                    x[n] = [1, 0]
                else:
                    # if a number and its double has been found
                    if x[n][1] == 1:
                        return True
                
                if 2 * n not in x:
                    x[2 * n] = [0, 1]
                else:
                    # if a number and its double has been found
                    if x[2 * n][0] == 1:
                        return True
            else:
                # special case for 0, since it is its own double
                if n not in x:
                    x[n] = 0
                else:
                    return True
        return False
