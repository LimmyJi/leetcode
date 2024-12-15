import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        # adj_matrix[i] will contain all (node, prob) pairs where node is adjacent to i
        adj_matrix = {}
        for i in range(n):
            adj_matrix[i] = []
        for i in range(len(edges)):
            adj_matrix[edges[i][0]].append((edges[i][1], succProb[i]))
            adj_matrix[edges[i][1]].append((edges[i][0], succProb[i]))

        pq = [(0, start_node)]
        # 1 - dist[v] is the max prob. from start_node to node v
        # dist[v] is the min prob of failing from start_node to v
        dist = [1 for _ in range(n)]
        dist[start_node] = 0

        # perform bfs with a queue
        while pq:
            entry = heapq.heappop(pq)
            cur_vertex = entry[1]
            # update dist for each neighbor
            for neighbor in adj_matrix[cur_vertex]:
                if 1 - dist[neighbor[0]] < (1 - dist[cur_vertex]) * neighbor[1]:
                    dist[neighbor[0]] = 1 - (1 - dist[cur_vertex]) * neighbor[1]
                    heapq.heappush(pq, (dist[neighbor[0]], neighbor[0]))
        
        return 1 - dist[end_node]
