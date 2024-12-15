class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # turn speed[i] = how many mins we have until monster i
        for i in range(len(speed)):
            if dist[i] % speed[i]:
                speed[i] = dist[i] // speed[i] + 1
            else:
                speed[i] = dist[i] // speed[i]

        # handle the faster monsters first
        speed.sort()
        ret = 0
        elapsed = 0
        for time in speed:
            if time <= elapsed:
                return ret
            else:
                ret = ret + 1
                elapsed = elapsed + 1
        
        return ret
