class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        added = 0  # flag indicating if we have added the new interval or not
        # for each interval
        for interval in intervals:
            # if the interval comes before new interval, just add it
            if (interval[0] < newInterval[0] and interval[1] < newInterval[0]):
                ret.append(interval)
            # if we havent added new interval yet, and we have found an interval that
            #   starts after new interval ends, add new interval, then add the existing interval
            elif (interval[0] > newInterval[1] and interval[1] > newInterval[1]):
                if added == 0:
                    ret.append(newInterval)
                    added = 1
                ret.append(interval)
            else:
                # else, the current interval overlaps with new interval, so merge them
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if added == 0:
            # if we havent added yet, just add to the end
            ret.append(newInterval)
        return ret
