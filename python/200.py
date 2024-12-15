class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ret = 0
        rows = len(grid)
        cols = len(grid[0])
        # nuke(r,c) will delete the whole island containing [r,c] recursively
        def nuke(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            nuke(r-1, c)
            nuke(r+1, c)
            nuke(r, c-1)
            nuke(r, c+1)
        # if we find land, nuke the whole island so we dont count it again
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ret += 1
                    nuke(r, c)
        return ret
