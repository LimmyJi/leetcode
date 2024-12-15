class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        # a, b prices of cheapest ones, with a < b
        a = prices[0]
        b = prices[1]
        if b < a:
            a = b
            b = prices[0]
        
        # find 2 cheapest
        for price in prices[2:]:
            if price < a:
                b = a
                a = price
            elif price < b:
                b = price
        
        # if we can buy
        if a + b > money:
            return money
        return money - a - b
