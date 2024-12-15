class Solution(object):
    #  will sort points based on x value
    def quicksort(self, points):
        n = len(points)
        if n <= 1:
            return points
        else:
            pivot = points[n/2]
            less = []
            more = []
            for i in range(n):
                if i != n/2:
                    if pivot[0] < points[i][0]:
                        more.append(points[i])
                    else:
                        less.append(points[i])
            return self.quicksort(less) + [pivot] + self.quicksort(more)
        
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        # can do better memory wise by computing in place mayb
        after_sort = self.quicksort(points)
        ret = 0
        # go thru these sorted points and find widest gap
        for i in range(n - 1):
            ret = max(ret, after_sort[i+1][0] - after_sort[i][0])
        return ret
