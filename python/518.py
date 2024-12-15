class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # backtrack_table[i] = self.change(i, coins)
        # this means our ans is backtrack_table[amount] 
        backtrack_table = [0] * (amount + 1)
        backtrack_table[0] = 1  # 1 way to make 0, []
        for coin in coins:
            # these j are all possible values less than amount that we can create by using atleast 1 copy of coin
            for j in range (coin, amount + 1):
                # if we can make j - coin N times, we can also make j N times by adding coin to all of the ways we can make j - coin
                backtrack_table[j] += backtrack_table[j - coin]
        # same logic as line 9
        return backtrack_table[amount]
