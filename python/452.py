class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort balloons by their start pos, breaking ties with end pos
        points.sort(key=lambda x: (x[0], x[1]))
        ret = 0
        # left and right represent the region an arrow can be shot
        #   to pop the current group of balloons, start with only the
        #   first balloon in the group
        left = points[0][0]
        right = points[0][1]
        # for next balloons, try to add it to the current group
        for point in points[1:]:
            # if we can find an area an arrow can be shot to pop the new balloon, and all
            #   the balloons in the current group
            if (point[0] >= left and point[0] <= right) or (point[1] <= right and point[1] >= left):
                left = max(point[0], left)
                right = min(point[1], right)
            else:
                # else pop the whole current group with 1 arrow, and start new group with just
                #   the new balloon
                ret += 1
                left = point[0]
                right = point[1]
        # +1 to pop the final group
        return ret + 1
