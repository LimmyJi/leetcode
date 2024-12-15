class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        # less_left[i] will count the number of indexs j < i such that
        #   rating[j] < rating[i]
        # more_right[i] ... j > i ... rating[j] > rating[i]
        # less_right[i] ... j > i ... rating[j] < rating[i]
        # more_left[i] ... j < i ... rating[j] > rating[i]
        less_left = [0 for _ in range(len(rating))]
        more_right = [0 for _ in range(len(rating))]
        less_right = [0 for _ in range(len(rating))]
        more_left = [0 for _ in range(len(rating))]
        for i in range(len(rating)):
            cur = rating[i]
            for j in range(i, len(rating)):
                if rating[j] > cur:
                    less_left[j] += 1
                    more_right[i] += 1
                elif rating[j] < cur:
                    less_right[i] += 1
                    more_left[j] += 1

        ret = 0
        # for the i-th soldier, use the created arrays to calculate how many teams can be in
        #   assuming the i-th soldier is in the middle
        for i in range(len(less_left)):
            ret += less_left[i] * more_right[i] + more_left[i] * less_right[i]

        return ret
