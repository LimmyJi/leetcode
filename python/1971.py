class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # lookup[i] will be an array with all the vertex adjacent to i
        lookup = [[] for _ in range(n)]
        for edge in edges:
            lookup[edge[0]].append(edge[1])
            lookup[edge[1]].append(edge[0])
        queue = []
        q_pos = 0
        queue.append(source)
        # use bfs w/ our edge lookup table
        while q_pos < len(queue):
            if queue[q_pos] == destination:
                return True
            # add all adjacent vertex to queue, and remove adjacency to mark as
            #   'visited'
            queue += lookup[queue[q_pos]]
            lookup[queue[q_pos]] = []
            q_pos += 1
        return False
