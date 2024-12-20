class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        num_row = len(obstacleGrid)
        num_col = len(obstacleGrid[0])
        # ans_grid[i][j] is the number of ways to get to (i, j)
        ans_grid = [[0 for i in range(num_col)] for j in range(num_row)]
        # 1 way to get to the start spot (we start here)
        ans_grid[0][0] = 1
        cur_row = 0
        cur_col = 0
        # fill out the ans_grid with dp, to get to (i, j), you either have
        #   to come from (i - 1, j) or (i, j - 1)
        while cur_row < num_row or cur_col < num_col:
            # fill out topmost unfilled row
            if cur_row < num_row:
                for i in range (cur_col, num_col):
                    if obstacleGrid[cur_row][i] == 1:
                        ans_grid[cur_row][i] = 0
                    else:
                        if cur_row - 1 >= 0:
                            ans_grid[cur_row][i] += ans_grid[cur_row - 1][i]
                        if i - 1 >= 0:
                            ans_grid[cur_row][i] += ans_grid[cur_row][i - 1]
            # fill out leftmost unfilled column
            if cur_col < num_col:
                for j in range (cur_row + 1, num_row):
                    if obstacleGrid[j][cur_col] == 1:
                        ans_grid[j][cur_col] = 0
                    else:
                        if cur_col - 1 >= 0:
                            ans_grid[j][cur_col] += ans_grid[j][cur_col - 1]
                        if j - 1 >= 0:
                            ans_grid[j][cur_col] += ans_grid[j - 1][cur_col]
            cur_row += 1
            cur_col += 1
        return ans_grid[num_row - 1][num_col - 1]
