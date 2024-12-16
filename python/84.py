class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heightss: List[int]
        :rtype: int
        """
        heights.append(0)  # append 0, so in the case all heights are increasing, we are forced to check at end
        # note:
        # if heights are in non-decreasing order, we can simply find
        #   the max area by multiplying the height of each bar by the
        #   # of bars w/ height geq to it.
        # let stack be the current set of bars in non-decreasing order
        stack = [-1]
        ans = 0
        # go thru each bar, force adding it to stack
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
