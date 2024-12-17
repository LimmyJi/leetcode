class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                for item in row:
                    if item == target:
                        return True
        return False
        """
        # binary search row bounds to determine which row may contain target
        num_rows = len(matrix)
        min_row = 0
        max_row = num_rows - 1
        while min_row != max_row:
            cur_row = (min_row + max_row) / 2
            if matrix[cur_row][-1] < target:
                min_row = cur_row + 1
            else:
                max_row = cur_row
        # now binary search this specific row
        num_col = len(matrix[0])
        min_col = 0
        max_col = num_col - 1
        while min_col != max_col:
            cur_col = (min_col + max_col) / 2
            if matrix[max_row][cur_col] == target:
                return True
            if matrix[max_row][cur_col] < target:
                min_col = cur_col + 1
            else:
                max_col = cur_col
        if matrix[max_row][max_col] == target:
            return True
        return False
