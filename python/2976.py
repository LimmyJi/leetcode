class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        # x[i][j] represents cost from changing a i to j, i != j
        x = [[-1 for _1 in range(26)] for _2 in range(26)]
        for _ in range(4):  # fill x out with depth of 4
            for i in range(len(cost)):
                og = ord(original[i]) - 97
                new = ord(changed[i]) - 97
                c = cost[i]
                if x[og][new] < 0 or x[og][new] > c:
                    x[og][new] = c
                for j in range(26):
                    if x[j][og] >= 0 and (x[j][og] + x[og][new] < x[j][new] or x[j][new] < 0):
                        x[j][new] = x[j][og] + x[og][new]

        # use our cost chart to see if our conversion is possible
        ret = 0
        for i in range(len(source)):
            have = ord(source[i]) - 97
            want = ord(target[i]) - 97
            if have == want:
                continue
            if x[have][want] < 0:
                return -1
            else:
                ret += x[have][want]
        return ret
