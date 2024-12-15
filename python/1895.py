class Solution(object):
    # check if a magic square of size nxn whose top right corner is at [sr, sc]
    def is_valid(self, sr, sc, n, grid):
        # get sum of first row, then brute force compute all other rows/cols/diagonals
        first_sum = sum(grid[sr][sc:sc+n])
        for i in range(1, n):
            if sum(grid[sr+i][sc:sc+n]) != first_sum:
                return False
        for i in range(n):
            col_sum = 0
            for j in range(n):
                col_sum += grid[sr+j][sc+i]
            if col_sum != first_sum:
                return False
        first_diag = 0
        second_diag = 0
        for i in range(n):
            first_diag += grid[sr+i][sc+i]
            second_diag += grid[sr+n-i-1][sc+i]
        if first_diag != first_sum:
            return False
        if second_diag != first_sum:
            return False
        return True

    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) # of rows
        n = len(grid[0]) # of cols
        max = min(m, n)
        # start searching w/ largest possible square size max, reduce down
        for i in range(0, max):
            starting_row = 0
            while starting_row + max - i <= m:
                starting_col = 0
                while starting_col + max - i <= n:
                    # first square found is max, since we start looking big
                    if self.is_valid(starting_row, starting_col, max - i, grid):
                        return max - i
                    starting_col += 1
                starting_row += 1
