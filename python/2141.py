class Solution(object):
    # if its possible to run n computers, w/ given batteries for specified
    #   runtime
    def possibleRunTime(self, n, batteries, run_time):
        total_min = 0
        for i in batteries:
            # if a battery lasts more than run_time, that extra power is useless
            total_min = total_min + min(i, run_time)

        min_per_comp = total_min / n
        if min_per_comp < run_time:
            return False
        return True

    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        total_power = 0
        for i in batteries:
            total_power += i
        # upper and lower bound on how long we can run for
        most_possible = total_power / n
        lowest_possible = 0
        batteries.sort()
        # then binary search possibilities, seeing what runtime is
        #   possible
        while most_possible - lowest_possible > 1:
            pivot = (most_possible + lowest_possible) / 2
            if self.possibleRunTime(n, batteries, pivot):
                lowest_possible = pivot
            else:
                most_possible = pivot - 1

        if self.possibleRunTime(n, batteries, most_possible):
            return most_possible
        else:
            return lowest_possible
