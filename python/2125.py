class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        ans = 0
        prev_row = 0
        cur_row = 0
        # for each row, get # of devices in the row
        for row in bank:
            for tile in row:
                if tile == '1':
                    cur_row += 1
            # if we find devices in current row, calculate # of lazers
            #   then set this row as the prev row
            if cur_row != 0:
                if prev_row != 0:
                    ans += cur_row * prev_row
                # only update prev row if cur row is non empty
                prev_row = cur_row
            cur_row = 0

        return ans
