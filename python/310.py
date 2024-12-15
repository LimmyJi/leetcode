class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # deg_counts[i] will store the degree of node i
        # neighbors[i] will store a list of neighbors of node i
        deg_counts = [0 for _ in range(n)]
        neighbors = [[] for _ in range(n)]
        for edge in edges:
            deg_counts[edge[0]] += 1
            deg_counts[edge[1]] += 1
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])

        count = n  # how many nodes are left in the ret_list
        # ret_list[i] = 1 if we return node i
        ret_list = [1 for _ in range(n)]
        while count > 2:
            to_remove = []
            # if a node has deg 1, it cant be a MHT since this means
            #   it has the height of another tree + 1
            for i in range(n):
                if deg_counts[i] == 1:
                    to_remove.append(i)
            
            # remove the nodes from the tree, their removal wouldnt matter since
            #   they are not the MHT, and they only have 1 neighbor so they wont effect the MHT outcome
            for node in to_remove:
                deg_counts[node] -= 1
                for neighbor in neighbors[node]:
                    deg_counts[neighbor] -= 1
                count -= 1
                ret_list[node] = 0

        # fill out ret based on ret_list once we lose enough nodes, note that a tree can only have a max
        #   of 2 MHTs, can prove via contradiction
        ret = []
        for i in range(n):
            if ret_list[i]:
                ret.append(i)
        return ret
