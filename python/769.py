class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        max_num = -1  # max number in current partition
        cur_count = -1  # how many in the current partition of the
        num_sorted = 0  # how many numbers have been sorted
        for i in range(len(arr)):
            # add to current partition if it is empty, manage max_num and cur_count
            if max_num == -1:
                max_num = arr[i]
                cur_count = 1
            elif arr[i] < max_num:
                cur_count += 1
            elif arr[i] > max_num:
                max_num = arr[i]
                cur_count += 1
            # if we have cur_count numbers in the current partition, and
            #   cur_count + num_sorted = max_num + 1, then we dont need to
            #   extend the partition
            if cur_count == max_num + 1 - num_sorted:
                ans += 1
                num_sorted = max_num + 1
                max_num = -1
        return ans
