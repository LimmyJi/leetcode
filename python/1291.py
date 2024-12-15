class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        ret = []
        base = 12  # since 10 <= low
        cur = base
        to_add = 11
        while cur <= high:
            # if cur is in bounds, add it to ret
            if cur >= low:
                ret.append(cur)
            if cur % 10 == 9:
                # if we need to add a digit, use this logic
                n = base % 10
                base *= 10
                base += n + 1
                cur = base
                to_add *= 10
                to_add += 1
            else:
                # increase by to_add to get next number
                cur += to_add
        return ret
