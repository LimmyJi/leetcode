class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        rows = len(land)
        cols = len(land[0])
        for r in range(rows):
            for c in range(cols):
                # if we find farmland, perform bfs in a southeast direction from the cell
                if land[r][c]:
                    cur_group = [r, c, -1, -1]
                    queue = []
                    q_pos = 0
                    queue.append((r, c))
                    while q_pos < len(queue):
                        cur_coord = queue[q_pos]
                        if cur_coord[0] < rows and cur_coord[1] < cols and land[cur_coord[0]][cur_coord[1]]:
                            land[cur_coord[0]][cur_coord[1]] = 0
                            # if we have reached edge of grid or found forest land, mark the edge of current farmland area
                            if (cur_coord[0] == rows - 1 or land[cur_coord[0] + 1][cur_coord[1]] == 0) and (cur_coord[1] == cols - 1 or land[cur_coord[0]][cur_coord[1] + 1] == 0):
                                cur_group[2] = cur_coord[0]
                                cur_group[3] = cur_coord[1]
                                break
                            else:
                                queue.append((cur_coord[0] + 1, cur_coord[1]))
                                queue.append((cur_coord[0], cur_coord[1] + 1))
                        q_pos += 1
                    if cur_group[2] < 0:
                        cur_group[2] = queue[-1][0]
                        cur_group[3] = queue[-1][1]
                    ret.append(cur_group)
        return ret                            
