class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0
        for stone in stones:
            # if the stone is also a jewel
            if stone in jewels:
                res += 1
        return res
