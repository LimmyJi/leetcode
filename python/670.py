class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # put the digits in an array
        temp = num
        digits = []
        while temp:
            digits = [temp % 10] + digits
            temp = temp // 10
        # sort the digits from largest to smallest, keeping track
        #   of the indexes that were sorted too
        indexs = range(0, len(digits))
        for i in range(len(digits)):
            largest = digits[i]
            largest_index = i
            for j in range(i + 1, len(digits)):
                if digits[j] > largest:
                    largest = digits[j]
                    largest_index = j

            temp = digits[largest_index]
            digits[largest_index] = digits[i]
            digits[i] = temp

            temp = indexs[largest_index]
            indexs[largest_index] = indexs[i]
            indexs[i] = temp

        # find the best swap - the earliest swap that was made
        to_swap = [-1, -1]
        for i in range(len(digits)):
            # if a swap happend at index i
            if indexs[i] > i:
                to_swap[0] = indexs[i]
                to_swap[1] = i
                for j in range(i + 1, len(digits)):
                    if digits[j] == digits[i]:
                        to_swap[0] = indexs[j]
                break

        # reconstruct num, with the desired single swapping found
        temp = num
        digits = []
        while temp:
            digits = [temp % 10] + digits
            temp = temp // 10
        if to_swap[1] >= 0:
            temp = digits[to_swap[0]]
            digits[to_swap[0]] = digits[to_swap[1]]
            digits[to_swap[1]] = temp
        ret = 0
        for i in digits:
            ret *= 10
            ret += i
        return ret
        