class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # count_dict[i] will have the # of roads connected to i
        # count_dict[i j] will have the # of roads connected to both i and j
        count_dict = {}
        for road in roads:
            if ("%d" % (road[0])) in count_dict:
                count_dict["%d" % (road[0])] += 1
            else:
                count_dict["%d" % (road[0])] = 1
            if ("%d" % (road[1])) in count_dict:
                count_dict["%d" % (road[1])] += 1
            else:
                count_dict["%d" % (road[1])] = 1
            if ("%d %d" % (min(road[0], road[1]), max(road[0], road[1]))) in count_dict:
                count_dict["%d %d" % (min(road[0], road[1]), max(road[0], road[1]))] += 1
            else:
                count_dict["%d %d" % (min(road[0], road[1]), max(road[0], road[1]))] = 1
        ans = 0
        # go through all possible pairs of cities, using count_dict to get network rank
        for i in range(n):
            for j in range(i + 1, n):
                net_rank = 0
                if ("%d" % (i)) in count_dict and ("%d" % (j)) in count_dict:
                    net_rank = count_dict["%d" % (i)] + count_dict["%d" % (j)]
                    if ("%d %d" % (i, j)) in count_dict:
                        net_rank -= count_dict["%d %d" % (i, j)]
                if net_rank > ans:
                    ans = net_rank
        return ans
