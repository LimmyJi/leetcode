class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 1:
            return 0

        ret = 0
        cur_section = 0
        # let left be the highest elevation we find to the left
        #   of the current bar
        # first, start at the leftmost bar, then search right
        # this will consider all the water that can be trapped to the left of
        #   the global maxima
        left = height[0]
        for bar in height[1:]:
            # if the current bar is geq left, we have found a right boundary for the
            #   trapped water, add it to ret, and make current bar our new left
            if bar >= left:
                left = bar
                ret += cur_section
                cur_section = 0
            else:
                # if current bar is less than left, that means left - bar units of
                #   water can be trapped ontop of it, if we find a right boundary for left
                cur_section += (left - bar)

        # do the same process, except start from the right, and look at bars going left
        # this will consider all the water that can be trapped to the right of
        #   the global maxima
        left = height[-1]
        cur_section = 0
        for bar in height[-2::-1]:
            if bar > left:
                left = bar
                ret += cur_section
                cur_section = 0
            else:
                cur_section += (left - bar)
        return ret
