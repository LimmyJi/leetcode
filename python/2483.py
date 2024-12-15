class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        y_ahead_count = 0
        n_behind_count = 0
        # let 0 be the penalty if we dont open at all
        min = 0
        ans = -1
        # for each hour, see if it is a Y or N, and calculate
        #   penalty w/ relativity to not opening it all
        for i in range(len(customers)):
            if customers[i] == 'N':
                n_behind_count += 1
            else:
                y_ahead_count -= 1
            penalty = n_behind_count + y_ahead_count
            if penalty < min:
                min = penalty
                ans = i
        return ans + 1
