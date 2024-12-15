class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        row = len(grid)
        col = len(grid[0])
        # search the grid from left to right and top to bottom
        for r in range(row):
            for c in range(col):
                # if we find land
                if grid[r][c]:
                    # add 4 to the perimeter
                    ret += 4
                    # however subtract some perimeter if it has neighbors to the
                    #   right or bottom
                    if r + 1 < row and grid[r + 1][c] == 1:
                        ret -= 2
                    if c + 1 < col and grid[r][c + 1] == 1:
                        ret -= 2
        return ret
