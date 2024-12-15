class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        wanted = tickets[k]
        ret = wanted
        # for person k to buy tickets:
        for i in range(k):
            # all people infront will have the opportunity to buy the same #
            ret += min(tickets[i], wanted)
        for i in range(k + 1, len(tickets)):
            # all people behind will have the opportunity to buy the same # - 1
            ret += min(tickets[i], wanted - 1)
        return ret
