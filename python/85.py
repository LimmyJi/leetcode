class Solution(object):
    # copied from 84
    def eval_hist(self, heights):
        heights.append(0)
        # note:
        # if heights are in non-decreasing order, we can simply find
        #   the max area by multiplying the height of each bar by the
        #   # of bars w/ height geq to it.
        # let stack be the current set of bars in non-decreasing order
        stack = [-1]
        ans = 0
        # go thru each bar, adding it to stack
        for i in range(len(heights)):
            # keep removing bars from the top of stack until the current bar is
            #   the largest
            while heights[i] < heights[stack[-1]]:
                # using our note, calculate the max area between [deleted bar, current bar).
                #   for each deleted bar
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ret = 0
        rows = len(matrix)
        cols = len(matrix[0])
        # hist[j] will keep track of the # of consecutive 1's in row j
        hist = [0 for _ in range(rows)]
        # go thru the cols, updating hist. we can treat the current col like the x axis on a graph,
        #   and hist[j] as the value for x = j
        # now we can use 84 to get the largest rectangle formed by starting from the current column, and only
        #   using columns to the left
        for i in range(cols):
            for j in range(rows):
                if matrix[j][i] == "1":
                    hist[j] += 1
                else:
                    hist[j] = 0
            cur = self.eval_hist(hist)
            if cur > ret:
                ret = cur
        return ret
