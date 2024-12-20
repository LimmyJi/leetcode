class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        # flag that indicates how we should update row and col
        direction = 'right'
        row = 0
        col = 0
        next_val = 1
        # while we have a valid unfilled square
        while row < n and col < n and res[row][col] == 0:
            # fill with the current value, then increment current value
            #   and update row/col according to the flag we defined
            res[row][col] = next_val
            next_val += 1
            if direction == 'right':
                if col + 1 < n and res[row][col + 1] == 0:
                    col += 1
                else:
                    direction = 'down'
                    row += 1
            elif direction == 'down':
                if row + 1 < n and res[row + 1][col] == 0:
                    row += 1
                else:
                    direction = 'left'
                    col -= 1
            elif direction == 'left':
                if col - 1 >= 0 and res[row][col - 1] == 0:
                    col -= 1
                else:
                    direction = 'up'
                    row -= 1
            elif direction == 'up':
                if row - 1 >= 0 and res[row - 1][col] == 0:
                    row -= 1
                else:
                    direction = 'right'
                    col += 1
        return res
